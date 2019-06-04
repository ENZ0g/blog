from django.shortcuts import render
from django.views.generic import ListView
from posts.models import Post
from django.views.generic.base import TemplateView


class PostsListView(ListView):
    queryset = Post.objects.filter(status="published")
    context_object_name = "posts"
    template = "posts/list.html"


class HowView(TemplateView):
    template_name = "posts/how.html"
