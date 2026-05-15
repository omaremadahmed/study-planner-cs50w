from django.shortcuts import render
from django.utils import timezone


def home(request):
    context = {}
    if request.user.is_authenticated:
        from tasks.models import Task
        from subjects.models import Subject

        tasks_qs = Task.objects.filter(user=request.user)
        today = timezone.localdate()
        pending = tasks_qs.filter(completed=False)

        context.update(
            {
                'total_tasks': tasks_qs.count(),
                'done_tasks': tasks_qs.filter(completed=True).count(),
                'pending_tasks': pending.count(),
                'overdue_tasks': pending.filter(
                    deadline__isnull=False,
                    deadline__lt=today,
                ).count(),
                'due_today_count': pending.filter(deadline=today).count(),
                'total_subjects': Subject.objects.filter(user=request.user).count(),
                'recent_tasks': tasks_qs.select_related('subject').order_by(
                    'deadline', 'title'
                )[:10],
            }
        )
    return render(request, 'planner/planner.html', context)


def pomodoro(request):
    return render(request, 'planner/pomodoro.html')
