from django.shortcuts import render

def blog(request):
    print('blog com render')
    return render(request, 'blog/blog.html')

def exemplo(request):
    print('exemplo do app blog')
    return render(request, 'blog/exemplo.html')