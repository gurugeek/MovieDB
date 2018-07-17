from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Comment
from .forms import MovieForm, CommentForm
from urllib.request import urlopen
import json

def index(request):
    return render(request, 'moviedbapp/index.html')

def movies(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            '''title for api call'''
            movietitle=request.POST.get('title')
            '''api call check if any spaces exist, change them to %20'''
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
                '''movie found? checking first if title has been saved before if not, saving form'''
                checkup = Movie.objects.filter(Title__iexact=movietitle).exists()
                if not checkup:
                    m = Movie(Title=Title, Year=Year, Released=Released, Genre=Genre, Director=Director, Plot=Plot, Poster=Poster)
                    m.save()
                else:
                    pass
            except KeyError:
                return render(request, 'moviedbapp/error.html')
            else:
                pass
        q=Movie.objects.get(Title__iexact=movietitle).id
        return redirect('detail', pk=q)
    else:
        form = MovieForm()
    return render(request, 'moviedbapp/movies.html')

def movieslist(request):
    films = Movie.objects.all()
    return render(request, 'moviedbapp/movieslist.html', {'films': films})

def comments(request):
    comments = Comment.objects.all()
    return render(request, 'moviedbapp/comments.html', {'comments':comments})

def detail(request, pk):
    '''comment adding section'''
    var = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.Title = var
            comment.save()
            return redirect('detail', pk=var.pk)
    else:
        form = CommentForm()
    '''displaying details'''
    movietitle = var.Title
    q = Movie.objects.get(Title__iexact=movietitle)
    titlee=q.Title
    year=q.Year
    released=q.Released
    genre=q.Genre
    director=q.Director
    plot=q.Plot
    poster=q.Poster
    return render(request, 'moviedbapp/moviedetails.html', {'form':form,'var':var,'titlee': titlee, 'year':year, 'released': released, 'genre':genre, 'director':director, 'plot': plot, 'poster':poster})
