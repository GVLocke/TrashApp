from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def index(response, name):
  ls = ToDoList.objects.get(name=name)
  return HttpResponse("<h1>%s</h1>" % ls.name)