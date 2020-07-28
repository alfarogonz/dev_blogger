

from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView


def home(request): #url patterns direct to these views, these handles the routes and return them
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context )


class PostListView(ListView):
    model = Post # what model to query in order to create list
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['date_posted']

class PostDetailView(DetailView):
    model = Post 

def about(request):
    return render(request, 'blog/about.html', {'title': ' About TITLE PASSED'})
