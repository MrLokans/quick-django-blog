from django.conf.urls import patterns, include, url

from .views import BlogIndex

urlpatterns = patterns(
    '',
    url(r'^$', BlogIndex.as_view(), name='index'),
)
