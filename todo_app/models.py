from django.db import models


status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class Task(models.Model):
    title = models.CharField(max_length=100,verbose_name='Название задачи')
    description = models.TextField(verbose_name='Описание задачи')
    extra_info = models.TextField(verbose_name='Дополнительное описание',null=True,blank=True)
    status = models.CharField(choices=status_choices, default=status_choices[0][0] , max_length=100,verbose_name='Выбор статуса')
    finish_date = models.DateField(null=True, blank=True,verbose_name='Дата выполнения задачи')

    def __str__(self):
        return f"{self.id} - {self.title}"

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'