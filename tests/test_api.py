import pytest
import sys

if sys.version_info >= (3, 6):
    try:
        from app import app  # 지우지 말 것
    except ModuleNotFoundError as e:
        import os

        myPath = os.path.dirname(os.path.abspath(__file__))
        sys.path.insert(0, myPath + '/../')
        from app import app
else:
    try:
        from app import app  # 지우지 말 것
    except ImportError as e:
        import os

        myPath = os.path.dirname(os.path.abspath(__file__))
        sys.path.insert(0, myPath + '/../')
        from app import app


def test_find_by_email_true(professors):
    with app.test_client() as mod:
        from flask import json
        email = 'professor1@professor.com'
        res = mod.post('find_by_email', data=dict(
            email=email
        ), follow_redirects=True)

        data = json.loads(res.data)

        assert data['user_exist'] == True


def test_find_by_email_false(professors):
    with app.test_client() as mod:
        from flask import json
        email = 'asdf@asdf.com'
        res = mod.post('find_by_email', data=dict(
            email=email
        ), follow_redirects=True)

        data = json.loads(res.data)

        assert data['user_exist'] == False


def test_accept_professor_post_success_accept(professors):
    with app.test_client() as mod:
        from flask import json
        from models.user import User

        email = 'professor1@professor.com'
        status = 'accept'
        res = mod.post('accept_professor', data=dict(
            email=email,
            status=status
        ), follow_redirects=True)

        data = json.loads(res.data)
        assert data['status'] == User.PROFESSOR_TYPE


def test_accept_professor_post_success_reject(professors):
    with app.test_client() as mod:
        from flask import json
        from models.user import User

        email = 'professor1@professor.com'
        status = 'reject'
        res = mod.post('accept_professor', data=dict(
            email=email,
            status=status
        ), follow_redirects=True)

        data = json.loads(res.data)
        assert data['status'] == User.PENDING_PROFESSOR_TYPE


def test_accept_professor_post_request_error(professors):
    with app.test_client() as mod:
        from flask import json

        email = 'professor1@professor.com'
        status = 'asdf'
        res = mod.post('accept_professor', data=dict(
            email=email,
            status=status
        ), follow_redirects=True)

        data = json.loads(res.data)
        assert data['status'] == 'request_error'


def test_accept_professor_post_fail(professors):
    with app.test_client() as mod:
        from flask import json
        email = 'asdf@asdf.com'
        status = 'accept'
        res = mod.post('accept_professor', data=dict(
            email=email,
            status=status
        ), follow_redirects=True)

        data = json.loads(res.data)
        assert data['msg'] == 'user_not_exist'
