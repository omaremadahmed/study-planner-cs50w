from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from subjects.models import Subject

from .models import Task


def _parse_deadline(post):
    raw = (post.get('deadline') or '').strip()
    if not raw:
        return None
    return datetime.strptime(raw, '%Y-%m-%d').date()

def _parse_positive_int(post, key):
    raw = (post.get(key) or '').strip()
    if not raw:
        return None
    try:
        value = int(raw)
    except ValueError:
        return None
    return value if value > 0 else None


def _subject_from_post(post, user):
    raw = (post.get('subject') or '').strip()
    if not raw:
        return None
    try:
        pk = int(raw)
    except ValueError:
        return None
    return Subject.objects.filter(pk=pk, user=user).first()

def _priority_from_post(post):
    raw = (post.get('priority') or '').strip().lower()
    valid = {choice[0] for choice in Task.Priority.choices}
    return raw if raw in valid else Task.Priority.MEDIUM


@login_required
def index(request):
    tasks = (
        Task.objects.filter(user=request.user)
        .select_related('subject')
        .order_by('completed', 'deadline', 'priority', 'title')
    )
    return render(request, 'tasks/index.html', {'tasks': tasks})


@login_required
def add_task(request):
    if request.method == 'POST':
        title = (request.POST.get('title') or '').strip()
        if title:
            deadline = None
            try:
                deadline = _parse_deadline(request.POST)
            except ValueError:
                pass
            Task.objects.create(
                user=request.user,
                title=title,
                notes=(request.POST.get('notes') or '').strip(),
                deadline=deadline,
                estimated_minutes=_parse_positive_int(request.POST, 'estimated_minutes'),
                priority=_priority_from_post(request.POST),
                subject=_subject_from_post(request.POST, request.user),
            )
            return redirect('task_list')
    subjects = Subject.objects.filter(user=request.user).order_by('name')
    return render(
        request,
        'tasks/add_task.html',
        {'subjects': subjects, 'priority_choices': Task.Priority.choices},
    )


@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        title = (request.POST.get('title') or '').strip()
        if title:
            task.title = title
            task.notes = (request.POST.get('notes') or '').strip()
            try:
                task.deadline = _parse_deadline(request.POST)
            except ValueError:
                task.deadline = None
            task.estimated_minutes = _parse_positive_int(request.POST, 'estimated_minutes')
            task.priority = _priority_from_post(request.POST)
            task.subject = _subject_from_post(request.POST, request.user)
            task.save()
            return redirect('task_list')
    subjects = Subject.objects.filter(user=request.user).order_by('name')
    return render(
        request,
        'tasks/edit_task.html',
        {'task': task, 'subjects': subjects, 'priority_choices': Task.Priority.choices},
    )


@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('task_list')


@login_required
def mark_task_done(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = True
    task.save(update_fields=['completed'])
    return redirect('task_list')


@login_required
def toggle_task_done(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save(update_fields=['completed'])
    return redirect('task_list')
