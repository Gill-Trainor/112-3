from django.contrib import admin
from .models import Genre, Movie, Delivery, GenreAdmin, MovieAdmin
# Register your models here.

admin.site.register(Genre, GenreAdmin)
admin.site.register(Delivery)
admin.site.register(Movie, MovieAdmin)