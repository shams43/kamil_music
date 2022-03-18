from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
from django.shortcuts import render

authors = {
    'Michael': "Michael's song",
    'John': "John's song",
}


# Create your views here.
def mainstr(request):
    data = {
        "authors_n": authors.keys()
    }
    return render(request, 'spotify/mainstr.html', context=data)


def getName(request, name):
    if authors.get(name):
        data = {
            "author": name,
            "song": authors[name]
        }
        return render(request, "spotify/songs.html", context=data)
    else:
        return HttpResponseRedirect('404')


def getNotFound(request):
    return HttpResponse(render_to_string('spotify/404.html'))



