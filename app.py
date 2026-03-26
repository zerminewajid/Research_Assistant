import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from rag.vectorstore import VectorStore
from pipeline.graph import build_graph

load_dotenv()

app = Flask(__name__)

print("[App] Initializing vector store...")
vectorstore = VectorStore()
print("[App] Building pipeline...")
pipeline = build_graph(vectorstore)
print("[App] Ready at http://localhost:5000")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/research", methods=["POST"])
def research():
    data = request.get_json()
    topic = data.get("topic", "").strip()
    if not topic:
        return jsonify({"error": "Please enter a topic."}), 400
    extra = data.get("extra_context", "").strip()
    if extra:
        vectorstore.add_texts([extra])
    try:
        result = pipeline.invoke({
            "topic": topic,
            "research_notes": "",
            "draft_report": "",
            "final_report": "",
            "error": None,
        })
        if result.get("error"):
            return jsonify({"error": result["error"]}), 500
        return jsonify({
            "final_report": result["final_report"],
            "research_notes": result["research_notes"],
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/detect-demo", methods=["POST"])
def detect_demo():
    """
    Uses the LLM to intelligently decide if a demo is possible
    for the given topic + report. Returns the demo type or null.
    """
    data = request.get_json()
    topic = data.get("topic", "").strip()
    report = data.get("report", "").strip()

    if not topic:
        return jsonify({"demo_type": None})

    from crewai import LLM
    llm = LLM(model="groq/llama-3.1-8b-instant", temperature=0)

    prompt = f"""You are an expert at identifying whether a research paper topic can be visualized interactively.

Research paper topic: "{topic}"

Brief report summary (first 500 chars): "{report[:500]}"

Your job: Decide if this research paper belongs to one of these specific interactive demo categories.
Each category has a specific visualization we can show:

- "transformer" → Papers about: Transformer architecture, self-attention, multi-head attention, BERT, GPT, positional encoding, encoder-decoder, attention mechanism
- "lstm" → Papers about: LSTM, GRU, RNN, recurrent neural networks, vanishing gradient, sequence modeling, memory gates
- "cnn" → Papers about: Convolutional neural networks, image classification, feature maps, pooling, AlexNet, VGG, ResNet, computer vision, object detection
- "federated" → Papers about: Federated learning, distributed training, privacy-preserving ML, FedAvg, non-IID data
- "rag" → Papers about: Retrieval-Augmented Generation, vector databases, semantic search, FAISS, embeddings, knowledge retrieval
- "mlops" → Papers about: MLOps, model deployment, CI/CD for ML, experiment tracking, model monitoring, MLflow

If the paper clearly belongs to one of these, respond with ONLY that one word.
If the paper is about something else entirely (economics, biology, social science, history, arts, food science, animal behavior, psychology, business, etc.), respond with ONLY the word: null

Do NOT force a match. Only return a category if the paper is genuinely and clearly about that specific technical topic.
Respond with ONE word only. No explanation. No punctuation."""

    try:
        response = llm.call(prompt)
        raw = str(response).strip().lower().split()[0] if response else "null"
        valid = {"transformer", "lstm", "cnn", "federated", "rag", "mlops"}
        demo_type = raw if raw in valid else None
        return jsonify({"demo_type": demo_type})
    except Exception as e:
        print(f"[detect-demo] Error: {e}")
        return jsonify({"demo_type": None})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
