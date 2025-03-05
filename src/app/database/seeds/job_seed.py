from app.database.factories.job_factory import JobFactory
from app.database.seeds import seed_actions
from app.database.seeds.base_seed import FactorySeeder


class Seeder(FactorySeeder):
    def __init__(self):
        super().__init__(name='JobSeeder', priority=1, factory=JobFactory)

    @seed_actions
    def seed(self, rows: int = 10):
        self.factory.create_batch(rows)
