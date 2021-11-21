from rest_framework import permissions, viewsets
from .models import Post 
from .serializers import PostSerializer, UserSerializer
from django.contrib.auth import get_user_model 


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

"""class PostList(generics.ListAPIView):
   permission_classes = (permissions.IsAuthenticated, )
   queryset = Post.objects.all()
   serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer"""