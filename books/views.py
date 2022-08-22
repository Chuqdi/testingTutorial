from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView
from .models import Book




def index(request):
    return render(request, 'index.html')

class CreateBook(CreateView):
    template_name ="create.html"
    fields="__all__"
    queryset = Book.objects.all()
    success_url = "/create_book"

class ListBooks(ListView):
    queryset= Book.objects.all()
    context_object_name ="books"
    template_name ="list.html"


class DeleteBook(DeleteView):
    template_name ="delete.html"
    success_url = "/list_book"
