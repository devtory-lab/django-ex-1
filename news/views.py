from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from news.models import Article


def index(request):
    year = '2020'
    messages = {
        '<a href="{}">{}년 게시물 보기</a><br><br>'.format(year, year),
        '<a href="{}/{}">{}년 11월 게시물 보기</a><br><br>'.format(year, 11, year),
        '<a href="{}/{}">{}년 10월 게시물 보기</a><br><br>'.format(year, 10, year),
    }
    return HttpResponse(messages)


def year_archive(request, year):
    year_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_year_list': year_list}
    return render(request, 'news/index.html', context)


def month_archive(request, year, month):
    month_list = Article.objects.filter(pub_date__year=year, pub_date__month=month)
    context = {'year': year, 'month': month, 'article_month_list': month_list}
    return render(request, 'news/list_month.html', context)


def detail(request, pk):
    t_article = get_object_or_404(Article, id=pk)
    context = {'article': t_article}
    return render(request, 'news/detail.html', context)
