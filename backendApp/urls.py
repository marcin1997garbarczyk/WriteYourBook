# api/urls.py
from django.urls import include, path

from backendApp.views import SubmitStoryFormView, SubmitAnswerFromUserView, GetMyStoriesView, GetStoryDetails, GetBalance

urlpatterns = [
    path('submit_story_form', SubmitStoryFormView.as_view(), name='submit_story_form'),
    path('submit_answer_from_user', SubmitAnswerFromUserView.as_view(), name='submit_answer_from_user'),
    path('get_my_stories', GetMyStoriesView.as_view(), name='get_my_stories'),
    path('get_story_details/<int:id>', GetStoryDetails.as_view(), name='get_story_details'),
    path('get_balance', GetBalance.as_view(), name='get_balance'),
]