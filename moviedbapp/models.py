from django.db import models

class Movie(models.Model):
    title = models.TextField(max_length=250, blank=True)

class Comment(models.Model):
    title = models.ForeignKey('moviedbapp.Movie', on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
