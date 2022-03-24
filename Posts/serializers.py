from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        field = ['id', 'author_id', 'title', 'url', 'creation_date']
