from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('post/<int:post_id>', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo'),
    path('', views.blog, name='blog'),
]
