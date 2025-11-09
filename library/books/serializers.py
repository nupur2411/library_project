from rest_framework import serializers
from .models import Author, Category, Book

class BookSerializer(serializers.ModelSerializer):
    Author = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = [ 'title', 'Author']
class CategorySerializer(serializers.ModelSerializer):
    books = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['id','name', 'book_count','books']
        
    