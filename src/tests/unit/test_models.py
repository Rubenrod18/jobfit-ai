from app.models.postgresql import User
from tests.common import fake


def test_create_user():
    data = {
        'name': fake.name(),
        'email': fake.email(),
    }

    user = User(**data)

    assert user.name == data['name']
    assert user.email == data['email']
