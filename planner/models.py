from django.conf import settings
from django.db import models


class StudySession(models.Model):
    class SessionType(models.TextChoices):
        POMODORO = 'pomodoro', 'Pomodoro'
        BREAK = 'break', 'Break'
        MANUAL = 'manual', 'Manual'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='study_sessions',
    )
    subject = models.ForeignKey(
        'subjects.Subject',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='study_sessions',
    )
    minutes = models.PositiveIntegerField()
    session_type = models.CharField(
        max_length=20,
        choices=SessionType.choices,
        default=SessionType.POMODORO,
    )
    started_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-started_at', '-created_at']

    def __str__(self):
        subj = self.subject.name if self.subject else 'No subject'
        return f'{self.user} - {subj} ({self.minutes}m)'
