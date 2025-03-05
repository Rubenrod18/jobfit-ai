from app.database.factories.resume_submission_factory import ResumeSubmissionFactory
from app.database.seeds import seed_actions
from app.database.seeds.base_seed import FactorySeeder


class Seeder(FactorySeeder):
    def __init__(self):
        super().__init__(name='ResumeSubmissionSeeder', priority=2, factory=ResumeSubmissionFactory)

    @seed_actions
    def seed(self, rows: int = 5):
        self.factory.create_batch(rows)
