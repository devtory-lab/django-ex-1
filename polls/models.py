import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    class Meta:
        db_table = 'TB_QUESTION'
        verbose_name = '질문목록'
        verbose_name_plural = '질문목록'

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:
        db_table = 'TB_QUESTION_CHOICE'
        verbose_name = '선택목록'
        verbose_name_plural = '선택목록'

    def __str__(self):
        return self.choice_text


