from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post 
from .serializers import PostSerializer

class PostList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

