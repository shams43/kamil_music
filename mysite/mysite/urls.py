
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('authors.urls')),
    path('admin/', admin.site.urls),

]
