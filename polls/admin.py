from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'pub_date')
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'choice_text', 'votes', 'question_id')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)