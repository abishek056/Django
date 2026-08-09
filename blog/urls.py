from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.index, name="home"),
    path("posts/", views.post_list, name="post_list"),
    path('post/new/', views.post_created, name='post_created'),
    path('post/<slug:slug>/', views.post_detail, name="post_detail"),
    path('about/', views.about, name='about'),
]


