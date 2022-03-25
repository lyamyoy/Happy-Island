from django.shortcuts import redirect, render
from django.views.generic import CreateView, TemplateView

from .models import Room, Post
# from cs50 import SQL

# db = SQL("sqlite:///db.sqlite3")

"""
class PostCreateView(CreateView):
    template_name = 'post_create.html' # PostCreateViewに紐づくテンプレートを表している
    form_class = PostForm # post_create.html内部でPostFormを用いた入力フォームを作成することができる
    success_url = reverse_lazy('post:post_create_complete') # 入力フォームを投稿した後に、遷移する url を指定


class PostCreateCompleteView(TemplateView):
    template_name = 'post_create_complete.html'
"""


# Create your views here.
def index(request):
  return redirect("../hello/login", {
    # "rooms": Room.objects.all()
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