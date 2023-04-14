from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.http import require_http_methods, require_safe, require_POST

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("movies:index")
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, "accounts/login.html", context)


@require_safe
def logout(request):
    auth_logout(request)
    return redirect("movies:index")


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("movies:index")
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, "accounts/signup.html", context)


@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("movies:index")
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form,
    }
    return render(request, "accounts/update.html", context)


@require_http_methods(['GET', 'POST'])
def password_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("movies:index")
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form,
    }
    return render(request, "accounts/password_change.html", context)


@require_safe
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect("movies:index")