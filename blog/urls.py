from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path('', PostListView.as_view() , name='blog-home'),
    path('post/<int:pk>', PostListView.as_view() , name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
