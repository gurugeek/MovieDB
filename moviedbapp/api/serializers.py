from rest_framework.serializers import ModelSerializer, SerializerMethodField
from moviedbapp.models import Movie, Comment


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'Title', 'Year', 'Released', 'Genre', 'Director', 'Plot', 'Poster',)

class CommentSerializer(ModelSerializer):
    Title = SerializerMethodField()
    class Meta:
        model = Comment
        fields = ('Title', 'comment')
    def get_Title(self, obj):
        return str(obj.Title.Title)

class MovieDetailSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'Title', 'Year', 'Released', 'Genre', 'Director', 'Plot', 'Poster',)

class CommentDetailSerializer(ModelSerializer):
    Title = SerializerMethodField()
    class Meta:
        model = Comment
        fields = ('Title', 'comment')
    def get_Title(self, obj):
        return str(obj.Title.Title)

class MovieCreateSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ('Title',)

class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('Title', 'comment')
