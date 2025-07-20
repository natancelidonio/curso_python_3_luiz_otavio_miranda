from django.shortcuts import render
from blog.data import posts


def blog(request):
    print('blog com template')
    context = {
        # 'text': 'Estamos no blog.',
        'head_title': 'Página do blog',
        'posts': posts,
    }
    return render(request, 'blog/blog.html', context)

def exemplo(request):
    print('exemplo do app blog')
    context = {
        'text': 'Isso é só um exemplo... !!',
        'head_title': 'Página de exemplo',
    }
    return render(request, 'blog/exemplo.html', context)