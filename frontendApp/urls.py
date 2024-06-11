from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('myStories', views.my_stories, name="myStories"),
    path('story/<int:id>', views.story, name="story"),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]