from rest_framework import serializers
from .models import Movie, Comment

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('title', 'comment')
