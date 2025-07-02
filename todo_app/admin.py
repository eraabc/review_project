from django.contrib import admin
from  .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status']
    list_filter = ['status']
    search_fields = ['title', 'description']
    fields = ['title', 'description', 'status', 'finish_date']

admin.site.register(Task,TaskAdmin)