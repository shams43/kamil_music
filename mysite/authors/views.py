from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
store = {
    'a': 'a, b, c',
    "b": "a"
}
def mainstr(request):
    return HttpResponse(render_to_string('authors/authors.html'))
def songs(request, name):
    if store.get(name):
        return HttpResponse(render_to_string('authors/songs.html'))
    else:
        return HttpResponseRedirect("404")
def getSongs(request):
        return HttpResponse(render_to_string('authors/albums.html'))
def NotFound(request):
    return HttpResponse(render_to_string('authors/404.html'))