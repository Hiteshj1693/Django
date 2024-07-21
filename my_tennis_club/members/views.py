from django.shortcuts import render, loader
from django.http import HttpResponse
# Create your views here.

def members(request):
    # return HttpResponse("Hello world!")
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())