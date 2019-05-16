######### first_app / views #########

from django.shortcuts import render, HttpResponse as hr, redirect as redir

# Create your views here.
def index(request):
    return hr("placeholder to later display a list of all blogs")

def new(request):
    return hr("placeholder to display a new form to create a new blog")

def create(request):
    return redir("/")

def show(request, number):
    return hr(f"placeholder to display blog number: {number}")

def edit(request, number):
    return hr(f"placeholder to edit blog {number}")

def destroy(request, number):
    return redir("/")