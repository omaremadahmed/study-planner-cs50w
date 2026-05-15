from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Subject


@login_required
def subjects_list(request):
    subjects = Subject.objects.filter(user=request.user)
    return render(request, 'subjects/subjects_list.html', {'subjects': subjects})


@login_required
def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk, user=request.user)
    tasks = (
        subject.tasks.filter(user=request.user)
        .select_related('subject')
        .order_by('deadline', 'title')
    )
    return render(
        request,
        'subjects/subject_detail.html',
        {'subject': subject, 'tasks': tasks},
    )


@login_required
def add_subject(request):
    if request.method == 'POST':
        name = (request.POST.get('name') or '').strip()
        if name:
            description = (request.POST.get('description') or '').strip()
            Subject.objects.create(
                user=request.user,
                name=name,
                description=description,
            )
            return redirect('subjects_list')
    return render(request, 'subjects/add_subject.html')


@login_required
def edit_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk, user=request.user)
    if request.method == 'POST':
        name = (request.POST.get('name') or '').strip()
        if name:
            subject.name = name
            subject.description = (request.POST.get('description') or '').strip()
            subject.save(update_fields=['name', 'description'])
            return redirect('subjects_list')
    return render(request, 'subjects/edit_subject.html', {'subject': subject})


@login_required
def delete_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk, user=request.user)
    subject.delete()
    return redirect('subjects_list')
