import pytest
from app import app  # 지우지 말 것


def test_set_check_password():
    from models.user import User

    password = 'skagustlfqkqh'
    user = User(user_num=12321312, name='JS Han', email='test@test.com', password=password, fingerprint='12321', type=1)
    assert user.check_password(password)


def test_create_user(session):
    from models.user import User
    password = 'skagustlfqkqh'
    user = User(user_num=12321312, name='JS Han', email='test@test.com', password=password, fingerprint='12321', type=1)

    user.create()
    assert user.id > 0


def test_find_user_by_email():
    from models.user import User
    user = User.find_by_email(email='test@test.com')
    assert user.email == 'test@test.com'
