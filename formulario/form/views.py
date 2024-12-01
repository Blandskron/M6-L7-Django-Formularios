from django.shortcuts import render, redirect
from .forms import AuthorForm, BookForm
from .models import Author, Book

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'form/author_form.html', {'form': form})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'form/author_list.html', {'authors': authors})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'form/book_form.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'form/book_list.html', {'books': books})