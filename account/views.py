from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserLoginForm, UserRegistrationForm, \
    UserEditForm, ProfileEditForm
from .models import Profile
from portfolio.models import Introduction


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            user_form.save()
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            Profile.objects.create(user=new_user)
            Introduction.objects.create(user=new_user)
            return redirect('account:login')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def edit(request, username):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            user = profile_form.save(commit=False)
            user.save()
            messages.success(request, 'Profile updated successfully')
            return redirect(user.get_account_absolute_url())
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form, 'title': 'Profile'})
