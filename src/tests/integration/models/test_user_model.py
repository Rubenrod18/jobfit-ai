from app.database.factories.user_factory import UserFactory
from tests.common import fake, session


class TestUserModel:
    def test_create_user(self):
        data = {
            'name': fake.name(),
            'email': fake.email(),
            'deleted_at': None,
        }

        user = UserFactory(**data)
        session.add(user)
        session.flush()

        assert user.name == data['name']
        assert user.email == data['email']
        assert user.created_at
        assert user.updated_at
        assert user.deleted_at is None
