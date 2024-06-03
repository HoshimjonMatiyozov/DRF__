from django.contrib import admin

# Register your models here.
from .models import Note

admin.site.register(Note)
# @admin.register(Note)
# class NoteAdmin(admin.ModelAdmin):
#     list_display=('title','owner','created','updated')
#     list_display_links=('title',)
#     search_fields=('title','owner','body')
#     list_filter=('created','updated')
    