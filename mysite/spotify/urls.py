from django.urls import path
from .views import *

urlpatterns = [
    path('addjanr/', add_janr, name='add_janr'),
    path('janrs', page_of_janrs,name="janrs"),
    path('addsong/', add_song, name='add_song'),
    path('addauthor/', add_author, name='add_author'),
    path('authors/',page_of_authors,name="authors"),
    path('songs/',page_of_songs,name="songs")



]
