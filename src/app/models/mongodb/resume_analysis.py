from datetime import datetime, UTC

from beanie import Document


class ResumeAnalysis(Document):
    user_id: int
    resume_text: str
    extracted_skills: list[str]
    suggestions: list[str]
    created_at: datetime = datetime.now(UTC)

    class Settings:
        collection = 'resume_analysis'
