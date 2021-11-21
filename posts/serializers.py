from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id', 
            'author', 
            'title', 
            'body', 
            'dists',
            'stats',
            'count',
            'created_at',
        )
        model = Post