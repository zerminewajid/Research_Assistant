from crewai import Agent, Task, Crew, Process, LLM
import os

def get_llm():
    return LLM(model="groq/llama-3.1-8b-instant", temperature=0.3)

def run_researcher(topic: str, context: str) -> str:
    llm = get_llm()
    researcher = Agent(
        role="Senior Research Analyst",
        goal="Thoroughly research and analyze the given topic, extracting key concepts, facts, and insights.",
        backstory="You are an expert research analyst with deep knowledge across science, technology, and academia. You excel at breaking down complex topics and gathering comprehensive information.",
        verbose=False,
        allow_delegation=False,
        llm=llm,
    )
    task = Task(
        description=(
            f"Research the following topic in depth: '{topic}'\n\n"
            f"Retrieved context from knowledge base:\n\n{context}\n\n"
            "Your job:\n"
            "1. Identify the 3-5 most important aspects of this topic\n"
            "2. Extract key facts, definitions, and concepts\n"
            "3. Note any important relationships or connections\n"
            "Produce detailed structured research notes."
        ),
        expected_output="Structured research notes covering key concepts, facts, and insights about the topic.",
        agent=researcher,
    )
    crew = Crew(agents=[researcher], tasks=[task], process=Process.sequential, verbose=False)
    return str(crew.kickoff())

def run_writer(topic: str, research_notes: str) -> str:
    llm = get_llm()
    writer = Agent(
        role="Expert Technical Writer",
        goal="Transform research notes into a clear, well-structured, and engaging report.",
        backstory="You are a skilled technical writer who specializes in making complex topics accessible. You produce reports that are accurate, well-organized, and easy to read.",
        verbose=False,
        allow_delegation=False,
        llm=llm,
    )
    task = Task(
        description=(
            f"Using the research notes below, write a comprehensive report on: '{topic}'\n\n"
            f"Research Notes:\n{research_notes}\n\n"
            "Structure your report with:\n"
            "## Overview\n## Key Concepts\n## Deep Dive\n## Applications & Relevance\n## Summary\n"
            "Write clearly and professionally. Aim for 400-600 words."
        ),
        expected_output="A well-structured markdown report with sections covering overview, key concepts, deep dive, applications, and summary.",
        agent=writer,
    )
    crew = Crew(agents=[writer], tasks=[task], process=Process.sequential, verbose=False)
    return str(crew.kickoff())

def run_critic(topic: str, draft: str) -> str:
    llm = get_llm()
    critic = Agent(
        role="Critical Review Editor",
        goal="Review, improve, and finalize the research report for accuracy, clarity, and completeness.",
        backstory="You are a meticulous editor with expertise in technical content. You identify gaps, fix inconsistencies, and ensure the report meets high standards.",
        verbose=False,
        allow_delegation=False,
        llm=llm,
    )
    task = Task(
        description=(
            f"Review and improve this research report on '{topic}':\n\n{draft}\n\n"
            "Your tasks:\n"
            "1. Fix any factual inaccuracies or unclear statements\n"
            "2. Improve flow and readability\n"
            "3. Add any missing critical information\n"
            "4. Add a 'Key Takeaways' section at the end with 3-5 bullet points\n"
            "Return the complete improved final report in markdown."
        ),
        expected_output="A polished, improved final report in markdown with a Key Takeaways section.",
        agent=critic,
    )
    crew = Crew(agents=[critic], tasks=[task], process=Process.sequential, verbose=False)
    return str(crew.kickoff())
