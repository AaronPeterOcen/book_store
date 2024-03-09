from django.shortcuts import render

from .models import Books

# Create your views here.
def index(request):
    """index func"""
    books = Books.objects.all()
    return render(request,"book_outlet/index.html", {
        "books": books
    })