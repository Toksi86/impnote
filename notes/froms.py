from django import forms

from .models import Topic, Note


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text']
        labels = {'title': 'Заголовок', 'text': 'Запись'}
        widget = {'test': forms.Textarea(attrs={'cols': 80})}
