from django.db import models

class Movie(models.Model):
    Title = models.TextField(max_length=250, blank=True)
    Year = models.TextField(blank=True)
    Released = models.TextField(blank=True)
    Genre = models.TextField(max_length=250, blank=True)
    Director = models.TextField(max_length=250, blank=True)
    Plot = models.TextField(max_length=1000, blank=True)
    Poster = models.URLField(default="http://google.com/")
    def __str__(self):
        return self.Title

class Comment(models.Model):
    Title = models.ForeignKey('moviedbapp.Movie', on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
