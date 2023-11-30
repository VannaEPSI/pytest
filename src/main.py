from src.services.book_fetcher_service import BookFetcherService
from src.services.book_service import BookService
from src.services.user_fetcher_service import UserFetcherService
from src.services.user_service import UserService

book_fetcher_service = BookFetcherService()
book_service = BookService(book_fetcher_service=book_fetcher_service)

print('ids : ' +  ', '.join(book_service.list_books_ids()))
print('authors : ' +  ', '.join(book_service.list_books_authors()))

user_fetcher_service = UserFetcherService()
user_service = UserService(user_fetcher_service=user_fetcher_service)
users = user_service.list_users()
for user in users:
    print (f'User mail : {user['email']} (id: {user['id']})')
