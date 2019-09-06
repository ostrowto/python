# views.py

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        id form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password_1')
        user = authenticate(username = username, password = raw_password)
        login(request, user)
        return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})