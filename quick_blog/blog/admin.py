from django.contrib import admin
from .models import Entry


class EntryAdmin(admin.ModelAdmin):

    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Entry, EntryAdmin)
