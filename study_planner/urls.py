from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('planner.urls')),
    path('tasks/', include('tasks.urls')),
    path('subjects/', include('subjects.urls')),
    path('users/', include('users.urls')),
]
