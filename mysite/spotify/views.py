from django.shortcuts import render, redirect

from .models import Song, Author, Janr
from .forms import AddSongForm, AddJanrForm, AddAuthorForm


def add_janr(request):
    if request.method == 'POST':
        form = AddJanrForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                print('something went wrong')
    else:
        form = AddJanrForm()
    return render(request, 'spotify/add_janr.html', {'form': form})

def add_song(request):
    if request.method == 'POST':
        form = AddSongForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                print('something went wrong')
    else:
        form = AddSongForm()
    return render(request, 'spotify/add_song.html', {"form": form})

def page_of_janrs(request):
    info=Janr.objects.all()
    return render(request, "spotify/janrs.html", {"info":info})

def add_author(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                print('something went wrong')
    else:
        form = AddAuthorForm()
    return render(request, 'spotify/add_author.html', {"form": form})
def page_of_authors(request):
    info=Author.objects.all()
    return render(request, "spotify/authors.html", {"info":info})
def page_of_songs(request):
    info=Song.objects.all()
    return render(request, "spotify/songs.html", {"info":info})