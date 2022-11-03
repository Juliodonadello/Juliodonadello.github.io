from django import views
from django.urls import path
from .views import render_posts

urlpatterns = [
    path('',render_posts,name='post'),
]

