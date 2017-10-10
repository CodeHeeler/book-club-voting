from django.shortcuts import render, redirect

from .models import Book
from .forms import BookForm


def book_list(request):
    return render(request, 'books/book_list.html', {
        'books': Book.objects.all(),
        'form': BookForm(),
    })


def new_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('book_list')
