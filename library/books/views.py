from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Author, Category, Book
from .serializers import  CategorySerializer, BookSerializer

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books': books})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'books/authors_list.html', {'authors': authors})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'books/categories_list.html', {'categories': categories})


class CategoryListView(ListAPIView):
    queryset = Category.objects.all().prefetch_related('book_set_author')
    serializer_class = CategorySerializer    