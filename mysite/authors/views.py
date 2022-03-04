from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
def mainstr(request):
    return HttpResponse(render_to_string('authors/bez_raznitsi.html'))