from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def members(request):
    # return HttpResponse("Hello world!")
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())
def index(request):
    return HttpResponse("Hello world!")
def home(request):
    return HttpResponse("Hello world!")
def about(request):
    return HttpResponse("Hello world!")
def contact(request):
    return HttpResponse("Hello world!")
def services(request):
    return HttpResponse("Hello world!")
def login(request):
    return HttpResponse("Hello world!")
def register(request):
    return HttpResponse("Hello world!")
def logout(request):
    return HttpResponse("Hello world!")
def profile(request):
    return HttpResponse("Hello world!")
def dashboard(request):
    return HttpResponse("Hello world!")
def add(request):
    return HttpResponse("Hello world!")
def view(request):
    return HttpResponse("Hello world!")
def delete(request):
    return HttpResponse("Hello world!")
def update(request):
    return HttpResponse("Hello world!")
def search(request):
    return HttpResponse("Hello world!")
def viewall(request):
    return HttpResponse("Hello world!")
def viewone(request):
    return HttpResponse("Hello world!")
def viewall(request):
    return HttpResponse("Hello world!")
