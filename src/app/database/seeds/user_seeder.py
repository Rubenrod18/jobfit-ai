from app.database.factories.user_factory import UserFactory
from app.database.seeds import seed_actions
from app.database.seeds.base_seed import FactorySeeder


class Seeder(FactorySeeder):
    def __init__(self):
        super().__init__(name='UserSeeder', priority=0, factory=UserFactory)

    @seed_actions
    def seed(self, rows: int = 10):
        self.factory.create_batch(rows)
