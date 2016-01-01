from django.conf.urls import patterns, include, url

from .views import BlogIndex, BlogDetail
from .feed import LatestPosts


urlpatterns = patterns(
    '',
    url(r'^$', BlogIndex.as_view(), name='index'),
    url(r'^feed/$', LatestPosts(), name="feed"),
    url(r'^(?P<slug>\S+)$', BlogDetail.as_view(), name="post_detail"),
)
