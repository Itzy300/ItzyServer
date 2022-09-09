from rest_framework import serializers

from users.serializers import ProfileGETSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    profile = ProfileGETSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ("pk", "profile", "title", "body", "image", "published_date", "likes", "category")


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "category", "body", "image")