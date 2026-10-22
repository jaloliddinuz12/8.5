from django.contrib import admin
from .models import Genre, Book, Comment

admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Comment)