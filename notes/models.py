from django.db import models


# Create your models here.
class Topic(models.Model):
    """Категория для записей"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Note(models.Model):
    """Запись в определённой категории"""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'notes'

    def __str__(self):
        return f'{self.text[:50]}...'
