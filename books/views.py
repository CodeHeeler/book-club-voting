from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404

from .models import Book
from .forms import BookForm


def book_edit_view (request, book_id):
    if request.method == 'POST':
        form = BookForm(request.POST, instance=get_object_or_404(Book, id=book_id))
        if form.is_valid():
            form.save()
        return redirect('book_list')
    else:
        book = get_object_or_404(Book, id=book_id)
        form = BookForm(instance=book)
        return render(request, "books/book_edit.html", {
            "form":form,
            "book_id": book_id,
        })


def book_delete_view (request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        book.delete()
        return redirect('book_list')
    else:
        book = get_object_or_404(Book, id=book_id)
        return render(request, "books/book_delete.html", {"book":book})


def book_list(request):
    books_all = Book.objects.all()
    paginator = Paginator(books_all, 20)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, 'books/book_list.html', {
        'books': books,
        'form': BookForm(),
    })


def new_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('book_list')
