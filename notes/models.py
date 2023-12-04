from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """Категория для записей"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')

    def __str__(self):
        return self.text


class Note(models.Model):
    """Запись в определённой категории"""

    title = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='notes')
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'notes'

    def __str__(self):
        return f'{self.text[:50]}...'
