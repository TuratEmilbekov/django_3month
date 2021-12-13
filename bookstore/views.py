from django.http.response import Http404
from django.shortcuts import render
from . import models
# Create your views here.
def get_books(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book': book})

def book_detail(request, id):
    try:
        book = models.Book.objects.get(id=id)
    except models.Book.DoesNotExist:
        raise Http404('Book does not exist, badboy')

    return render(request, 'book_detail.html', {'book':book})