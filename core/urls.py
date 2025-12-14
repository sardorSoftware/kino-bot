from django.contrib import admin
from django.urls import path
from movies.api import get_movie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/movie/', get_movie),
]
