# -*- coding: utf-8 -*-
from django.db import models

class City(models.Model):
    name = models.CharField( u"имя", max_length = 140,
            blank=True, null=True)
    
    class Meta:
        verbose_name = u"Город"
        verbose_name_plural = u"Города"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Partner(models.Model):
    pos = models.IntegerField(u"позиция",default=0)
    show = models.BooleanField(u"отображать", default = True) 
    name = models.CharField( u"имя", max_length = 140,
            blank=True, null=True)
    city = models.ForeignKey(City, default = 0)
    url = models.CharField( u"ссылка", max_length = 250,
            blank=True, null=True)
    antey = models.BooleanField(u"алмаз-антей", default = False) 
    
    class Meta:
        verbose_name = u"Партнёр"
        verbose_name_plural = u"Партнёры"
        ordering = ["pos"]

    def __str__(self):
        return self.name

