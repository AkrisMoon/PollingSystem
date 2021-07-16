from rest_framework import serializers
from .models import Polls, Questions, Answers, UsersAnswers

class PollsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polls
        fields = '__all__'


class PollDetailSerializer(serializers.ModelSerializer):
    start = serializers.HiddenField(default=Polls.start)

    class Meta:
        model = Polls
        fields = '__all__'


class PollsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polls
        fields = '__all__'


class QuestionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'


class QuestionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'


class AnswerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = '__all__'


class UsersAnswerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersAnswers
        fields = '__all__'


class UsersAnswersListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = UsersAnswers