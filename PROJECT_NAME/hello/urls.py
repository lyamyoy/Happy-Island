from django.urls import path
from . import views
from .views import Create

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('list/', views.list, name='list'),
    path('logout/', views.user_logout, name='logout'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('good/<int:pk>', views.good, name='good'),
    path('create/', Create.as_view(), name='create')
]