from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# Create your views here.
# def post_list(request):
#     """Display a list of all the posts."""
#     posts = Post.objects.all()
#     return render(request, 'posts/post_list.html', {'posts' : posts})


class PostList(ListView):
    model = Post
    template_name = "posts/post_list.html"
