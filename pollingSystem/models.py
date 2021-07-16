from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()


class Polls(models.Model):
    name = models.CharField(verbose_name='Poll name', max_length=255)
    start = models.DateTimeField(verbose_name='Start date', default=timezone.now)
    end = models.DateTimeField(verbose_name='End date')
    description = models.TextField(verbose_name='Description')


class Questions(models.Model):
    poll = models.ForeignKey(Polls, verbose_name='Question poll', on_delete=models.CASCADE)
    text = models.CharField(verbose_name='Question text', max_length=255)
    type = models.CharField(verbose_name='Question type',
                           max_length=23,
                           choices=[('text', 'Text answer'),
                                    ('chose_one', 'Answer with one choise'),
                                    ('chose_many', 'Answer with many choise'),
                                    ])


class Answers(models.Model):
    question = models.ForeignKey(Questions, verbose_name='Answer question', on_delete=models.CASCADE)
    answer = models.TextField(verbose_name='Answer')


class UsersAnswers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Polls, verbose_name= 'Passed poll', on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, verbose_name='Answered question', on_delete=models.CASCADE)
    answer = models.ForeignKey(Answers, verbose_name='User answer', on_delete=models.CASCADE)