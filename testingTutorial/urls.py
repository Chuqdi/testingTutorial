

from django.contrib import admin
from django.urls import path
from books.views import CreateBook, DeleteBook, ListBooks, index

urlpatterns = [
    path("", index, name="index"),
    path('admin/', admin.site.urls),
    path("create_book", CreateBook.as_view(), name="create_book"),
    path("list_book", ListBooks.as_view(), name="list_book"),
    path("delete_book/<int:pk>/", DeleteBook.as_view(), name="delete_book"),
]
