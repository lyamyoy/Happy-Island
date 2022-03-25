from django.contrib import admin

from .models import Room, User, Post

# Register your models here.
admin.site.register(Room)
admin.site.register(User)
admin.site.register(Post)