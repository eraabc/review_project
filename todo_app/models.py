from django.db import models
from pytils.translit import slugify


class Task(models.Model):
    title = models.CharField(max_length=100,verbose_name='Название задачи',unique=True)
    description = models.TextField(verbose_name='Описание',null=True,blank=True)
    status = models.ForeignKey('todo_app.Status',on_delete=models.PROTECT,verbose_name='Статус',related_name='tasks')
    type = models.ForeignKey('todo_app.Type',on_delete=models.PROTECT,verbose_name='Тип',related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Время обновления')
    slug = models.SlugField(max_length=100,verbose_name='Слаг',blank=True,null=True,unique=True)


    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)


    def __str__(self):
        return f"{self.title} - {self.status.title}"

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Status(models.Model):
    title = models.CharField(max_length=100,verbose_name='Статус',unique=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'statuses'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Type(models.Model):
    title = models.CharField(max_length=100,verbose_name='Статус',unique=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'types'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'