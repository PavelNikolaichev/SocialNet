from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source='author_id.id')

    class Meta:
        model = Post
        fields = ['id', 'author_id', 'title', 'url', 'creation_date']
