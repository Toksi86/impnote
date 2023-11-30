"""Определяет схемы URL для notes."""

from django.urls import path

from . import views

app_name = 'notes'
urlpatterns = [path('', views.index, name='index'),
               path('topics/', views.get_topics, name='topics'),
               path('topics/<int:topic_id>/', views.get_topic, name='topic'),
               ]
