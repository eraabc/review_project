from django.contrib import admin
from  .models import Task,Type,Status

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status']
    list_filter = ['status']
    search_fields = ['title', 'description']
    exclude = ['slug']

admin.site.register(Task,TaskAdmin)
admin.site.register(Type)
admin.site.register(Status)