from django.shortcuts import render
from django.http import   HttpResponse
from .models import *
from django.shortcuts import HttpResponseRedirect 
# Create your views here.


def index(request):
     return HttpResponse ('Hello world')
def book_list(request):
     context={}
     books = Book.objects.all()
     context['books'] = books

     return render(request,'book/list.html',context)
     # return HttpResponse ('book list')
def book_add(request):
     return render(request,'book/add.html')
     # return HttpResponse ('book add')
def book_update(request,name):
     return HttpResponse (f'book update {name}')

def book_delete(request,id):
      Book.objects.filter(id=id).delete()
      return HttpResponseRedirect ('/book/list')


     # return HttpResponse (f'book delete {id}')

def book_show(request,id):
          context={'book':Book.objects.get(id=id)}
          return render(request,'book/details.html',context)
          # return HttpResponse (f'book show {id}')
