from django.db import models
from django.core.urlresolvers import reverse


from django_markdown.models import MarkdownField


class Tag(models.Model):

    slug = models.SlugField(max_length=180, unique=True)

    def __str__(self):
        return self.slug


class EntryQuerySet(models.QuerySet):

    def published(self):
        """Return published blog entries"""
        return self.filter(published=True)


class Entry(models.Model):

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
        ordering = ["-created"]

    title = models.CharField(max_length=180)
    body = MarkdownField()
    # field to store human-readable urls
    slug = models.SlugField(max_length=180, unique=True)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    # we extand filtering methods this way
    objects = EntryQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

