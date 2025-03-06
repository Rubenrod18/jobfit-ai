from datetime import datetime, UTC

from beanie import Document


class JobAnalysis(Document):
    job_id: int
    job_description: str
    required_skills: list[str]
    ai_summary: str
    created_at: datetime = datetime.now(UTC)

    class Settings:
        collection = 'job_analysis'
