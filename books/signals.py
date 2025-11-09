from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Book, Author, Category

def update_counts(book,action):
    category = book.category
    author= book.author
    category.book_count = Book.objects.filter(category=category).count()
    author.total_books = Book.objects.filter(author=author).count()
    category.save()
    author.save()

@receiver(post_save, sender=Book)
def update_counts_on_save(sender, instance, created, **kwargs):
    update_counts(instance,'save')

@receiver(post_delete, sender=Book)
def update_counts_on_delete(sender, instance, **kwargs):
    update_counts(instance,'delete')