from django.urls import path
from spotify import views

urlpatterns = [
    path('', views.mainstr, ),
    path('404', views.getNotFound),
    path('<name>', views.getName),


]
