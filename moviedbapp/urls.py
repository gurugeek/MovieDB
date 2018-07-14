from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^movies$', views.movies, name='movies'),
url(r'^movies-list$', views.movieslist, name='movieslist'),
url(r'^comments$', views.comments, name='comments'),
url(r'^detail/(?P<pk>\d+)$', views.detail, name='detail'),
url(r'^detail$', views.detail, name='detail'),
]
