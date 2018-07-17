from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from moviedbapp.models import Movie, Comment
from .serializers import MovieSerializer, CommentSerializer, MovieDetailSerializer, CommentDetailSerializer, MovieCreateSerializer, CommentCreateSerializer

'''list'''
class MovieList(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class CommentList(ListAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self, *args, **kwargs):
        queryset_list = Comment.objects.all()
        query = self.request.GET.get('title')
        if query:
            queryset_list = queryset_list.filter(Title__iexact=query)
        return queryset_list

'''detail'''
class MovieDetail(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer

class CommentDetail(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer

'''create'''
class MovieCreate(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieCreateSerializer

class CommentCreate(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
