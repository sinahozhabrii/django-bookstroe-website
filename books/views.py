from django.shortcuts import render
from django.views import generic

from books.models import Book


# Create your views here.
class BookListView(generic.ListView):
    model = Book
    template_name = "books/books_list_view.html"
    context_object_name = "books"
class BookDetailView(generic.DetailView):
    model = Book
    template_name = "books/books_detail_view.html"

class BookCreateView(generic.edit.CreateView):
    model = Book
    fields = ['title', 'author', 'content', 'price']
    template_name = 'books/books_create.html'

class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'content', 'price']
    template_name = "books/books_update.html"