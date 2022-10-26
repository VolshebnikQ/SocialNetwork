from datetime import date
from django.utils import timezone
from django.db import models

from .slugify import slugify
from apps.profile.models import User


class City(models.Model):
    """Город"""
    title = models.CharField(max_length=255, verbose_name='Название города')
    slug = models.SlugField(blank=True, unique=True, verbose_name="url")

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(City, self).save(*args, **kwargs)


class Message(models.Model):
    """Сообщение"""
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    message_text = models.TextField('Текст сообщения')
    message_image = models.ImageField(
        'Изображение',
        blank=True,
        upload_to='images/messages/')
    date = models.DateTimeField('Дата',default=timezone.now) 
 
    class Meta:
        ordering = ('date', )
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'{self.city} - {self.date} - {self.user}'
