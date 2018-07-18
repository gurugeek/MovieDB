from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from moviedbapp.models import Movie, Comment
from .serializers import MovieSerializer, CommentSerializer, MovieDetailSerializer, CommentDetailSerializer, MovieCreateSerializer, CommentCreateSerializer
from urllib.request import urlopen
import json

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
            queryset_list = queryset_list.filter(Title_id=query)
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
    def perform_create(self, serializer):
        movietitle=self.request.POST.get('Title')
        url = "http://omdbapi.com/?t="+movietitle.replace(" ", "%20")+"&apikey=88f5ce43"
        data = json.loads(urlopen(url).read().decode('utf-8'))
        try:
            Title=data['Title']
            Year=data['Year']
            Released=data['Released']
            Genre=data['Genre']
            Director=data['Director']
            Plot=data['Plot']
            Poster=data['Poster']
            checkup = Movie.objects.filter(Title__iexact=movietitle).exists()
            if not checkup:
                serializer.save(Title=Title, Year=Year, Released=Released, Genre=Genre, Director=Director, Plot=Plot, Poster=Poster)
            else:
                pass
        except KeyError:
            pass
        else:
            pass

class CommentCreate(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
