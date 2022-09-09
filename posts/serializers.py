from rest_framework import serializers

from users.serializers import ProfileGETSerializer
from .models import Post,Comment


class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileGETSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ("pk", "profile", "post", "text")


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post", "text")


class PostSerializer(serializers.ModelSerializer):
    profile = ProfileGETSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("pk", "profile", "title", "body", "image",
                  "published_date", "likes", "category", "comments")


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "category", "body", "image")