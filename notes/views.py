from django.shortcuts import render, redirect

from .froms import TopicForm, NoteForm
from .models import Topic, Note


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


def new_topic(request):
    """Создание нового раздела"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:topics')
    context = {'form': form}
    return render(request, 'notes/new_topic.html', context)


def new_note(request, topic_id):
    """Создание новой записи"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = NoteForm()
    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.topic = topic
            new_note.save()
            return redirect('notes:topic', topic_id=topic_id)
    context = {'topic': topic, 'form': form}
    return render(request, 'notes/new_note.html', context)


def edit_note(request, note_id):
    """Изменение записи"""
    note = Note.objects.get(id=note_id)
    topic = note.topic

    if request.method != 'POST':
        form = NoteForm(instance=note)
    else:
        form = NoteForm(instance=note, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:topic', topic_id=topic.id)
    context = {'note': note, 'topic': topic, 'form': form}
    return render(request, 'notes/edit_note.html', context)
