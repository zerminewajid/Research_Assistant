from langgraph.graph import StateGraph, END
from .state import ResearchState
from .agents import run_researcher, run_writer, run_critic

def researcher_node(state: ResearchState, vectorstore) -> ResearchState:
    print(f"[Step 1/3] Researcher Agent: {state['topic']}")
    try:
        context = vectorstore.search(state["topic"], k=5)
        notes = run_researcher(state["topic"], context)
        return {**state, "research_notes": notes}
    except Exception as e:
        return {**state, "error": f"Researcher failed: {str(e)}"}

def writer_node(state: ResearchState) -> ResearchState:
    print("[Step 2/3] Writer Agent")
    try:
        draft = run_writer(state["topic"], state["research_notes"])
        return {**state, "draft_report": draft}
    except Exception as e:
        return {**state, "error": f"Writer failed: {str(e)}"}

def critic_node(state: ResearchState) -> ResearchState:
    print("[Step 3/3] Critic Agent")
    try:
        final = run_critic(state["topic"], state["draft_report"])
        return {**state, "final_report": final}
    except Exception as e:
        return {**state, "error": f"Critic failed: {str(e)}"}

def should_continue(state: ResearchState) -> str:
    return "end" if state.get("error") else "continue"

def build_graph(vectorstore):
    graph = StateGraph(ResearchState)
    graph.add_node("researcher", lambda s: researcher_node(s, vectorstore))
    graph.add_node("writer", writer_node)
    graph.add_node("critic", critic_node)
    graph.set_entry_point("researcher")
    graph.add_conditional_edges("researcher", should_continue, {"continue": "writer", "end": END})
    graph.add_conditional_edges("writer", should_continue, {"continue": "critic", "end": END})
    graph.add_edge("critic", END)
    return graph.compile()
