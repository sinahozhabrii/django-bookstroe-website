from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404,render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from books.models import Book
from books.forms import CommentForm


# Create your views here.
class BookListView(generic.ListView):
    model = Book
    paginate_by = 6
    template_name = "books/books_list_view.html"
    context_object_name = "books"
# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = "books/books_detail_view.html"
@login_required
def detail_view(request,pk):
    book = get_object_or_404(Book, pk=pk)
    books_comment = book.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request,'books/books_detail_view.html',{
        'book':book,
        'comment_form':comment_form,
        'comments':books_comment

    })


class BookCreateView(LoginRequiredMixin,generic.edit.CreateView):
    model = Book
    fields = ['title', 'author', 'content', 'price','cover']
    template_name = 'books/books_create.html'

class BookUpdateView(LoginRequiredMixin,UserPassesTestMixin,generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'content', 'price',"cover"]
    template_name = "books/books_update.html"
    def test_func(self):
        obj = self.get_object()
        return

class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/books_delete.html'
    success_url = reverse_lazy('book_list')
