import datetime

from django.contrib import admin

# Register your models here.
from django.utils import timezone

from polls.models import Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['question_text']
    list_display = ('id', 'question_text', 'pub_date')
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'choice_text', 'votes', 'question_id')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)