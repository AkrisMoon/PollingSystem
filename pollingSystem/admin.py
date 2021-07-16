from django.contrib import admin
from pollingSystem import models

@admin.decorators.register(models.Polls)
class PollsAdmin(admin.ModelAdmin):
    pass

@admin.decorators.register(models.Questions)
class QuestionsAdmin(admin.ModelAdmin):
    pass

@admin.decorators.register(models.Answers)
class AnswersAdmin(admin.ModelAdmin):
    pass

@admin.decorators.register(models.UsersAnswers)
class UsersAnswersAdmin(admin.ModelAdmin):
    pass

