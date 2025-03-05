import random
from datetime import timedelta

import factory

from app.database.factories.base_factory import BaseFactory, faker
from app.database.factories.job_factory import JobFactory
from app.database.factories.user_factory import UserFactory
from app.models.postgresql.user import ResumeSubmission


class ResumeSubmissionFactory(BaseFactory):
    class Meta:
        model = ResumeSubmission

    user = factory.SubFactory(UserFactory)
    job = factory.SubFactory(JobFactory)

    resume_text = factory.Faker('paragraph')
    submission_date = faker.date_time_between(start_date='-3y', end_date='now')
    score = factory.LazyFunction(lambda: round(random.uniform(0, 100), 2))

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
