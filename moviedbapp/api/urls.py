from django.conf.urls import url
from .views import (
    MovieList,
    CommentList,
    MovieDetail,
    CommentDetail,
    MovieCreate,
    CommentCreate,
)



urlpatterns = [
url(r'^movie$', MovieList.as_view()),
url(r'^movie/$', MovieList.as_view()),
url(r'^comment$', CommentList.as_view()),
url(r'^comment/$', CommentList.as_view()),
url(r'^movie/(?P<pk>\d+)$', MovieDetail.as_view()),
url(r'^movie/(?P<pk>\d+)/$', MovieDetail.as_view()),
url(r'^comment/(?P<pk>\d+)/$', CommentDetail.as_view()),
url(r'^comment/(?P<pk>\d+)$', CommentDetail.as_view()),
url(r'^movie/create$', MovieCreate.as_view()),
url(r'^movie/create/$', MovieCreate.as_view()),
url(r'^comment/create$', CommentCreate.as_view()),
url(r'^comment/create/$', CommentCreate.as_view()),
]
