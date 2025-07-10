from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blog(request):
    print('blog do app')
    return HttpResponse('blog do app')

def exemplo(request):
    print('exemplo do app blog')
    return HttpResponse('exemplo do app blog')