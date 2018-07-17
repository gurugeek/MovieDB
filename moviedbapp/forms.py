from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('Title',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
