from django.contrib import admin

from django_markdown.admin import MarkdownModelAdmin

from .models import Entry, Tag


class EntryAdmin(MarkdownModelAdmin):

    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag)
