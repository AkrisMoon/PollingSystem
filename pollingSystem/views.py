from django.utils import timezone

from rest_framework import generics, permissions
from rest_framework.response import Response

from .serializers import *
from pollingSystem.models import User, Polls, Questions, Answers


class PollsListView(generics.ListAPIView):
    serializer_class = PollsListSerializer
    queryset = Polls.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class PollsActiveListView(generics.ListAPIView):
    serializer_class = PollsListSerializer
    queryset = Polls.objects.filter(end__gte=timezone.now(),
                                   start__lte=timezone.now())


class PollsCreateView(generics.CreateAPIView):
    serializer_class = PollsCreateSerializer
    permission_classes = (permissions.IsAdminUser,)


class PollDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PollDetailSerializer
    queryset = Polls.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class QuestionsListView(generics.ListAPIView):
    serializer_class = QuestionsListSerializer
    queryset = Questions.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class QuestionsCreateView(generics.CreateAPIView):
    serializer_class = QuestionDetailSerializer
    permission_classes = (permissions.IsAdminUser,)


class QuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionDetailSerializer
    queryset = Questions.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class AnswersCreateView(generics.CreateAPIView):
    serializer_class = AnswerDetailSerializer
    permission_classes = (permissions.IsAdminUser,)


class AnswerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnswerDetailSerializer
    queryset = Answers.objects.all()
    permission_classes = (permissions.IsAdminUser,)


class UsersAnswersCreateView(generics.GenericAPIView):
    serializer_class = UsersAnswerDetailSerializer

    def post(self, request):
        answer = UsersAnswerDetailSerializer(data=request.data, context=request)
        if answer.is_valid(raise_exception=True):
            answer.save()
            return Response({'result': 'OK'})


class UsersAnswersListView(generics.ListAPIView):
    serializer_class = UsersAnswersListSerializer

    def get_queryset(self):
        queryset = UsersAnswers.objects.filter(user=self.request.user)
        return queryset


class UsersAnswersIDListView(generics.ListAPIView):
    serializer_class = UsersAnswersListSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get_queryset(self):
        queryset = UsersAnswers.objects.filter(user=User.objects.get(id=self.kwargs.get('pk')))
        return queryset