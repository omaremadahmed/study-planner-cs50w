from django.conf import settings
from django.db import models


class Subject(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='subjects',
    )
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=7, blank=True, help_text='Hex color like #3b82f6')
    weekly_target_minutes = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
