from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def say_hello(request):
    return HttpResponse('Hy i am testing my site')

# === THIS FILE IS MORE LIKE A REQUEST HANDLERS ===

def secretPage(request):
    res=HttpResponse('Not Found', status=404)
    return res