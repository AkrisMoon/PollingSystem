from django.urls import path
from pollingSystem.views import *

app_name = 'pollingSystem'
urlpatterns = [
    path('polls/create/', PollsCreateView.as_view()),
    path('polls/list/', PollsListView.as_view()),
    path('polls/active/', PollsActiveListView.as_view()),
    path('poll/detail/<int:pk>/', PollDetailView.as_view()),

    path('questions/create/', QuestionsCreateView.as_view()),
    path('questions/list/', QuestionsListView.as_view()),
    path('questions/detail/<int:pk>/', QuestionDetailView.as_view()),

    path('answers/create/', AnswersCreateView.as_view()),
    path('answer/detail/<int:pk>/', AnswerDetailView.as_view()),

    path('user_answers/create/', UsersAnswersCreateView.as_view()),
    path('user_answers/list/', UsersAnswersListView.as_view()),
    path('user_answers/<int:pk>/', UsersAnswersIDListView.as_view()),
]