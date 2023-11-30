import collections

from src.services.user_fetcher_service import UserFetcherService
from src.services.user_service import UserService


def test_list_users(monkeypatch):
    # we define a function that will replace the existing function
    # instead of calling the mocked server, we use a controlled dataset
    def mock_get_users(*args):
        return [
            {'id': 1, 'email': 'lyly@epsi.com'},
            {'id': 2, 'email': 'tantan@epsi.com'}
        ]

    monkeypatch.setattr(UserFetcherService, 'get_users', mock_get_users)

    user_service = UserService(user_fetcher_service=UserFetcherService())
    list = user_service.list_users()

    assert list == [{'id': 1, 'email': 'lyly@epsi.com'}, {'id': 2, 'email': 'tantan@epsi.com'}]


def test_list_users_with_no_id(monkeypatch):
    # we define a function that will replace the existing function
    # instead of calling the mocked server, we use a controlled dataset
    def mock_get_users(*args):
        return [
            {'id': '', 'email': 'lyly@epsi.com'},
            {'id': 2, 'email': 'tantan@epsi.com'}
        ]

    monkeypatch.setattr(UserFetcherService, 'get_users', mock_get_users)

    user_service = UserService(user_fetcher_service=UserFetcherService())
    list = user_service.list_users()

    assert list == [{'id': '', 'email': 'lyly@epsi.com'}, {'id': 2, 'email': 'tantan@epsi.com'}]

def test_list_users_no_email(monkeypatch):
    # we define a function that will replace the existing function
    # instead of calling the mocked server, we use a controlled dataset
    def mock_get_users(*args):
        return [
            {'id': 1, 'email': ''},
            {'id': 2, 'email': 'tantan@epsi.com'}
        ]

    monkeypatch.setattr(UserFetcherService, 'get_users', mock_get_users)

    user_service = UserService(user_fetcher_service=UserFetcherService())
    list = user_service.list_users()

    assert list == [{'id': 1, 'email': ''}, {'id': 2, 'email': 'tantan@epsi.com'}]

def test_list_users_no_user(monkeypatch):
    # we define a function that will replace the existing function
    # instead of calling the mocked server, we use a controlled dataset
    def mock_get_users(*args):
        return [
            {'id': '', 'email': ''}
        ]

    monkeypatch.setattr(UserFetcherService, 'get_users', mock_get_users)

    user_service = UserService(user_fetcher_service=UserFetcherService())
    list = user_service.list_users()

    assert list == [{'id': '', 'email': ''}]
