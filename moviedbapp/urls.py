from django.conf.urls import url
from . import views
from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('movie', views.MovieView)
router.register('comment', views.CommentView)

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^movies$', views.movies, name='movies'),
url(r'^movies-list$', views.movieslist, name='movieslist'),
url(r'^comments$', views.comments, name='comments'),
url(r'^detail/(?P<pk>\d+)$', views.detail, name='detail'),
url(r'^detail$', views.detail, name='detail'),
url(r'', include(router.urls)),
]
