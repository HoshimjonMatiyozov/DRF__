from django.urls import path

from . import views

urlpatterns = [
    path ('users/',views.get_notes),
    path('notes/new/',views.create_note),
    path('user/',views.create_note)
]