from django.shortcuts import render

from .models import Topic


def index(request):
    """Домашняя страница приложения notes"""
    return render(request, 'notes/index.html')


def get_topics(request):
    """Выводит список разделов."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'notes/topics.html', context)


def get_topic(request, topic_id):
    """Выводит раздел и все его записи"""
    topic = Topic.objects.get(id=topic_id)
    # Модели Topic и Note связаны. Экземпляра класса Topic имеет метод,
    # позволяющий получить все связанные объекты класса Note, при помощи classname_set
    notes = topic.note_set.order_by('-date_added')
    context = {'topic': topic, 'notes': notes}
    return render(request, 'notes/topic.html', context)
