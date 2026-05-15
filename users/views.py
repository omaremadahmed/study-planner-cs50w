from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = (request.POST.get('username') or '').strip()
        email = (request.POST.get('email') or '').strip()
        password1 = request.POST.get('password1') or ''
        password2 = request.POST.get('password2') or ''
        if password1 != password2:
            return render(
                request,
                'users/register.html',
                {'error': 'Passwords do not match.'},
            )
        if User.objects.filter(username=username).exists():
            return render(
                request,
                'users/register.html',
                {'error': 'Username already taken.'},
            )
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
        )
        auth_login(request, user)
        return redirect('home')
    return render(request, 'users/register.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = (request.POST.get('username') or '').strip()
        password = request.POST.get('password') or ''
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        return render(
            request,
            'users/login.html',
            {'error': 'Invalid username or password.'},
        )
    return render(request, 'users/login.html')


def logout_view(request):
    auth_logout(request)
    return redirect('home')
