from django.contrib import admin
from  .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status']
    list_filter = ['status']
    search_fields = ['title', 'description']

admin.site.register(Task,TaskAdmin)