from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('myStories', views.myStories, name="myStories"),
    path('story/<int:id>', views.story, name="story"),
]