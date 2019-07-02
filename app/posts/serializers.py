from django.contrib.auth import get_user_model  # In case we will want to change default User model to custom
from rest_framework import serializers
from .models import Post

__all__ = ['PostSerializer']


UserModel = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True, source='user.username')
    title = serializers.CharField(max_length=50)
    body = serializers.CharField(max_length=500)
    likes_count = serializers.IntegerField(
        source='likes.count',
        read_only=True
    )

    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'body', 'created_at', 'likes_count',)
