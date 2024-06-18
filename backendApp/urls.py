# api/urls.py
from django.urls import include, path

from backendApp.views import create_story, submit_answer, get_my_stories, get_story_details, get_balance

urlpatterns = [
    path('submit_story_form', create_story.as_view(), name='submit_story_form'),
    path('submit_answer_from_user', submit_answer.as_view(), name='submit_answer_from_user'),
    path('get_my_stories', get_my_stories.as_view(), name='get_my_stories'),
    path('get_story_details/<int:id>', get_story_details.as_view(), name='get_story_details'),
    path('get_balance', get_balance.as_view(), name='get_balance'),
]