from django.shortcuts import render

from .models import Room, Post
# from cs50 import SQL

# db = SQL("sqlite:///db.sqlite3")

# Create your views here.
def index(request):
  return render(request, "rooms/index.html", {
    "rooms": Room.objects.all()
  })


def room(request, room_id):
  room = Room.objects.get(pk=room_id)
  post = Post.objects.filter(where_id=room_id).order_by('-id')
  return render(request, "rooms/room.html", {
    "room": room,
    "posts": post
  })


def post(request):
  return render(request, "rooms/post.html")