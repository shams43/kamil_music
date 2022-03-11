from django.urls import path
from . import views
urlpatterns=[
    path('',views.mainstr),
    path('404',views.NotFound),
    path('songs',views.getSongs),
    path('<name>',views.songs)
]