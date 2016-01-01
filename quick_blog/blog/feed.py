from django.contrib.syndication.views import Feed

from .models import Entry


class LatestPosts(Feed):
    title = "QuickBlog"
    link = "/feed/"
    description = "Latest Posts"

    def items(self):
        return Entry.objects.published()[:10]
