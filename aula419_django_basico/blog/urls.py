from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('exemplo/', views.exemplo, name='exemplo'),
    path('post/<id>', views.post, name='post'),
]
