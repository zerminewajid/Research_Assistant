from typing import TypedDict, Optional

class ResearchState(TypedDict):
    topic: str
    research_notes: str
    draft_report: str
    final_report: str
    error: Optional[str]
