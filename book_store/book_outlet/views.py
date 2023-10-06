from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404
from django.db.models import Avg

def index(request):
    books = Book.objects.all().order_by('-rating') # minus means descending
    return render(request, 'book_outlet/index.html', {
        'books': books,
        'total': books.count,
        'average_rating': books.aggregate(Avg('rating'))['rating__avg']
    })

#def book_detail(request, id):
def book_detail(request, slug):
    try:
        # book = Book.objects.get(pk=id)
        book = Book.objects.get(slug=slug)
    except:
        raise Http404()
    #book = get_object_or_404(Book, pk=id) # another alternative how to raise 404 if book does not exist
    return render(request, 'book_outlet/book_detail.html', {
        'title': book.title,
        'author': book.author,
        'rating': book.rating,
        'is_bestseller': book.is_bestselling
    })
