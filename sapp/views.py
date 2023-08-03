from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def books(request):
    return render(request, 'books.html')

def book(request):
    return render(request, 'book.html')

def contact(request):
    return render(request, 'contact.html')

def base(request):
    return render(request, 'base.html')

def details(request):
    return render(request, 'details.html')

def index(request):
    return render(request, 'index.html')

from sapp.models import Book

def book(request):
    book=Book.objects.all()
    context={'book':book}
    return render(request,'book.html',context)