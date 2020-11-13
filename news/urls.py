from django.urls import path

from news import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:year>/', views.year_archive, name='year_list'),
    path('<int:year>/<int:month>', views.month_archive, name='month_list'),
    path('<int:pk>/detail/', views.detail, name='detail'),
]