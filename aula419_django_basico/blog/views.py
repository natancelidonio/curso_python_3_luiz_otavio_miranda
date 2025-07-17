from django.shortcuts import render

def blog(request):
    print('blog com template')
    context = {
        'text': 'Estamos na home, my brother!',
        'title': 'Página do blog',
    }
    return render(request, 'blog/blog.html', context)

def exemplo(request):
    print('exemplo do app blog')
    context = {
        'text': 'Estamos na home, my brother!',
        'title': 'Página de exemplo',
    }
    return render(request, 'blog/exemplo.html', context)