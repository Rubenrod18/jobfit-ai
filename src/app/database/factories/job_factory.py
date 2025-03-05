import random
from datetime import timedelta

import factory

from app.database.factories.base_factory import BaseFactory, faker
from app.models.postgresql import Job


class JobFactory(BaseFactory):
    class Meta:
        model = Job

    title = factory.Faker('job')
    description = factory.Faker('text')
    required_skills = factory.Faker('words', nb=3)
    company = factory.Faker('company')
    posted_at = faker.date_time_between(start_date='-3y', end_date='now')

    @factory.lazy_attribute
    def created_at(self):
        return faker.date_time_between(start_date='-3y', end_date='now')

    @factory.lazy_attribute
    def deleted_at(self):
        return random.choice([faker.date_time_between(start_date='-1y', end_date='now'), None])

    @factory.lazy_attribute
    def updated_at(self):
        if self.deleted_at:
            updated_at = self.deleted_at
        else:
            updated_at = self.created_at + timedelta(days=random.randint(1, 30), minutes=random.randint(0, 60))

        return updated_at
