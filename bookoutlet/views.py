from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Books

# Create your views here.
def index(request):
    """index func"""
    books = Books.objects.all()
    return render(request,"book_outlet/index.html", {
        "books": books
    })

def book_detail(request, slug):
    # try:
    #     book = Books.objects.get(pk=id)
    # except:
    #     raise Http404()
    # alternative for 404 error
    book = get_object_or_404(Books, slug=slug)
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "ratings":book.ratings,
        "is_bestseller":book.is_bestselling
    })
    