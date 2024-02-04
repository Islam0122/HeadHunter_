from django.db import models
from django.urls import reverse

from apps.Basemodel.models import BaseModel


class MenuItem(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Название')
    url = models.CharField(max_length=255, verbose_name='URL')
    named_url = models.CharField(max_length=255, verbose_name='Название URL', blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE,
                               verbose_name='Родительский пункт')

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.title
