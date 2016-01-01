from django.conf.urls import patterns, include, url

from .views import BlogIndex
from .feed import LatestPosts


urlpatterns = patterns(
    '',
    url(r'^$', BlogIndex.as_view(), name='index'),
    url(r'^feed/$', LatestPosts(), name="feed"),
)
