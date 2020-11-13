from django.db import models


class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = '작성자목록'
        verbose_name_plural = '작성자목록'


class Article(models.Model):
    pub_date = models.DateTimeField(verbose_name='작성일시')
    headline = models.CharField(max_length=200, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE, verbose_name='작성자명')

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = '기사목록'
        verbose_name_plural = '기사목록'
        ordering = ('-pub_date', '-pk')
