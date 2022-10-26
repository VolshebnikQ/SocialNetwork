from datetime import date

from django.db import models

from apps.profile.models import User


class Post(models.Model):
    """Пост"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField('Дата', default=date.today)
    content = models.TextField('Содержимое')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'{self.user}-{self.date}'
