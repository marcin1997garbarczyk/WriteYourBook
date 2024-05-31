# api/urls.py
from django.urls import include, path

from backendApp.views import SubmitStoryFormView, SubmitAnswerFromUserView

urlpatterns = [
    path('submit_story_form', SubmitStoryFormView.as_view(), name='submit_story_form'),
    path('submit_answer_from_user', SubmitAnswerFromUserView.as_view(), name='submit_answer_from_user'),
]