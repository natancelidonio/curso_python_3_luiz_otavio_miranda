from django.shortcuts import render

def home(request):
    print('home com render')
    context = {
        'text': 'Estamos na home, my brother!',
        'title': 'Página Inicial',
    }
    return render(
        request,
        'home/index.html',
        context,
    )