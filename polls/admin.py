from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'pub_date')


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'choice_text', 'votes', 'question_id')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)