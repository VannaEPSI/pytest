from src.services.book_fetcher_service import BookFetcherService
from src.services.book_service import BookService
from Tools.outils import comparaison_tableau


def test_list_book_ids(monkeypatch):
    # we define a function that will replace the existing function
    # instead of calling the mocked server, we use a controlled dataset
    def mock_get_books(*args):
        return [
            {'id': 'aaa-001', 'name': 'Origine', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
            {'id': 'aaa-002', 'name': 'Anges & Démons', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
        ]

    monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_books)

    book_service = BookService(book_fetcher_service=BookFetcherService())
    ids = book_service.list_books_ids()

    assert ids == ['aaa-001', 'aaa-002']


def test_list_authors(monkeypatch):
    def mock_get_books(*args):
        return [
            {'id': 'aaa-001', 'name': 'Origine', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
            {'id': 'aaa-002', 'name': 'Anges & Démons', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
        ]

    monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_books)

    book_service = BookService(book_fetcher_service=BookFetcherService())
    authors = book_service.list_books_authors()

    assert authors == ['Brown Dan']

def test_list_book_name_empty(monkeypatch):
    # we define a function that will replace the existing function
    # instead of calling the mocked server, we use a controlled dataset
    def mock_get_books(*args):
        return [
            {'id': 'aaa-001', 'name': '', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
            {'id': 'aaa-002', 'name': 'Anges & Démons', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
        ]

    monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_books)

    book_service = BookService(book_fetcher_service=BookFetcherService())
    name_empty = book_service.list_books_name()

    assert name_empty == ['', 'Anges & Démons']


def test_list_book_ids_empty(monkeypatch):
    # we define a function that will replace the existing function
    # instead of calling the mocked server, we use a controlled dataset
    def mock_get_books(*args):
        return [
            {'id': '', 'name': 'Origine', 'author': {'firstname': 'Dan', 'lastname': 'Brownie'}},
            {'id': 'aaa-002', 'name': 'Anges & Démons', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
        ]

    monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_books)

    book_service = BookService(book_fetcher_service=BookFetcherService())
    ids_empty = book_service.list_books_ids()

    assert ids_empty == ['', 'aaa-002']

def test_list_authors_with_no_first_name(monkeypatch):
    def mock_get_books(*args):
        return [
            {'id': 'aaa-001', 'name': 'Origine', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
            {'id': 'aaa-002', 'name': 'Anges & Démons', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
            {'id': 'aaa-003', 'name': 'Zen', 'author': {'firstname': '', 'lastname': 'Jaegger'}},
        ]

    monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_books)

    book_service = BookService(book_fetcher_service=BookFetcherService())

    authors = book_service.list_books_authors()
    assert comparaison_tableau(authors) == comparaison_tableau(['Brown Dan', 'Jaegger '])


def test_list_authors_with_no_author(monkeypatch):
    def mock_get_books(*args):
        return [
            {'id': 'aaa-001', 'name': 'Origine', 'author': {'firstname': '', 'lastname': ''}},
            {'id': 'aaa-002', 'name': 'vava', 'author': {'firstname': '', 'lastname': ''}},
        ]

    monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_books)

    book_service = BookService(book_fetcher_service=BookFetcherService())

    authors = book_service.list_books_authors()
    assert comparaison_tableau(authors) == comparaison_tableau([' '])


def test_list_authors_one_book(monkeypatch):
    def mock_get_books(*args):
        return [
            {'id': 'aaa-001', 'name': 'Origine', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}}
        ]

    monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_books)

    book_service = BookService(book_fetcher_service=BookFetcherService())

    authors = book_service.list_books_authors()
    assert comparaison_tableau(authors) == comparaison_tableau(['Brown Dan'])


def test_list_authors_one_author(monkeypatch):
    def mock_get_books(*args):
        return [
            {'id': 'aaa-001', 'name': 'Origine', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
            {'id': 'aaa-002', 'name': 'vava', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},
            {'id': 'aaa-003', 'name': 'tata', 'author': {'firstname': 'Dan', 'lastname': 'Brown'}},

        ]

    monkeypatch.setattr(BookFetcherService, 'get_books', mock_get_books)

    book_service = BookService(book_fetcher_service=BookFetcherService())

    authors = book_service.list_books_authors()
    assert comparaison_tableau(authors) == comparaison_tableau(['Brown Dan'])