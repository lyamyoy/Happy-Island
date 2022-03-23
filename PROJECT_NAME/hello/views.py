from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import Model
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'hello/signup.html', {'some': 100})
        except IntegrityError:
            return render(request, 'hello/signup.html', {'error': 'このユーザーはすでに登録されています'})
    return render(request, 'hello/signup.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('list')

        else:
            # Return an 'invalid login' error message.
            return render(request, 'hello/login.html', {})
    return render(request, 'hello/login.html', {})

def list(request):
    object_list = Model.objects.all()
    print(object_list)
    return render(request, 'hello/list.html', {'object_list': object_list})

def user_logout(request):
    logout(request)
    return redirect('login')

def detail(request, pk):
    object = get_object_or_404(Model, pk=pk)
    return render(request, 'hello/detail.html', {'object': object})

def good(request, pk):
    print("ここまで！！")
    object = Model.objects.get(pk=pk)
    object.good = int(object.good) + 1
    print("ここまで！！")
    object.save()
    return redirect('list')

class Create(CreateView):
    template_name = 'hello/create.html'
    model = Model
    fields = ('title', 'content', 'author', 'image')
    success_url = reverse_lazy('list')


















