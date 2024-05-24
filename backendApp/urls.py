# api/urls.py
from django.urls import include, path

from backendApp.views import SubmitStoryFormView

urlpatterns = [
    path('submit_story_form', SubmitStoryFormView.as_view(), name='submit_story_form'),
]