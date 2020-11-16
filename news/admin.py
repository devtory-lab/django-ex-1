from django.contrib import admin
from .models import Article, Reporter


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['headline']
    list_display = ('id', 'headline', 'reporter', 'pub_date')
    list_display_links = ('id', 'headline')


class ReporterAdmin(admin.ModelAdmin):
    search_fields = ['full_name']
    list_display = ('id', 'full_name')
    list_display_links = ('id', 'full_name')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Reporter, ReporterAdmin)
