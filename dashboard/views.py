from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from .models import UserProfile, LearningPath, Resource, Progress



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'dashboard/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'dashboard/login.html', {'form': form})

def dashboard(request):
    user_profile = UserProfile.objects.get(user=request.user)
    learning_paths = LearningPath.objects.filter(user=request.user)
    progress = Progress.objects.filter(user=request.user)

    context = {
        'user_profile': user_profile,
        'learning_paths': learning_paths,
        'progress': progress,
    }
    return render(request, 'dashboard/dashboard.html', context)

