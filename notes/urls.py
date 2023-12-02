"""Определяет схемы URL для notes."""

from django.urls import path

from . import views

app_name = 'notes'
urlpatterns = [path('', views.index, name='index'),
               path('topics/', views.get_topics, name='topics'),
               path('topics/<int:topic_id>/', views.get_topic, name='topic'),
               path('new_topic/', views.new_topic, name='new_topic'),
               path('new_note/<int:topic_id>/', views.new_note, name='new_note'),
               path('edit_note/<int:note_id>/', views.edit_note, name='edit_note'),
]
