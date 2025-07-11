from django.shortcuts import render

def home(request):
    print('home com render')
    return render(request, 'home/index.html')