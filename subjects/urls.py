from django.urls import path

from . import views

urlpatterns = [
    path('', views.subjects_list, name='subjects_list'),
    path('add/', views.add_subject, name='add_subject'),
    path('<int:pk>/', views.subject_detail, name='subject_detail'),
    path('<int:pk>/edit/', views.edit_subject, name='edit_subject'),
    path('<int:pk>/delete/', views.delete_subject, name='delete_subject'),
]
