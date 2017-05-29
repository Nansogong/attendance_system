import pytest


@pytest.fixture(scope='session', autouse=True)
def session():
    from models.user import db

    """Creates a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session
    yield
    transaction.rollback()
    connection.close()
    session.remove()


@pytest.fixture(scope='session')
def user():
    from models.user import User
    password = 'alskdjfhghfj'
    _user = User(user_num=1234321, name='Pro fessor', email='professor@professor.com', password=password,
                fingerprint='13531', type=User.PROFESSOR_TYPE)
    _user.create()
    yield _user


@pytest.fixture(scope='session')
def lecture(user):
    from models.lecture import Lecture
    _lecture = Lecture(professor_id=user.id, name="SWE", lecture_code="12364")
    _lecture.create()
    yield _lecture
