from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import render


def home(request):
    posts = Post.objects.all().order_by("-created_at")  # Fetch all posts
    return render(request, "home.html", {"posts": posts})
