from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'user', 'deadline', 'completed', 'id')
    list_filter = ('completed', 'user')
