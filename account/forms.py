from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'full-width', 'placeholder': ('Username')}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'full-width', 'placeholder': ('Password')}))
# class UserLoginForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         super(UserLoginForm, self).__init__(*args, **kwargs)
#     username = forms.CharField(required=True, widget=forms.TextInput(
#         attrs={'class': ('full-width'), 'placeholder': ("Enter your username")}))
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={'class': ('full-width'), 'placeholder': ("Enter your password")}))


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'full-width', 'placeholder': ('Username')}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'full-width', 'placeholder': ('First Name')}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'full-width', 'placeholder': ('Last Name')}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'full-width', 'placeholder': ('Email')}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': ('full-width'), 'placeholder': ("Enter your password")}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(
        attrs={'class': ('full-width'), 'placeholder': ("Confirm your password")}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class UserEditForm(forms.ModelForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': ('full-width')}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': ('full-width'), 'placeholder': ('First Name')}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': ('full-width'), 'placeholder': ('Last Name')}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': ('full-width')}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileEditForm(forms.ModelForm):
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'class': 'full-width'}))
    #profile_pics = forms.FileField(required=True, widget=forms.FileInput(attrs={'class': 'full-width'}))
    bio = forms.CharField(widget=CKEditorWidget(config_name='awesome_ckeditor'))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'full-width', 'placeholder': ('Phone number. e.g. +23480612345')}))
    twitter_url = forms.CharField(widget=forms.TextInput(attrs={'class':'full-width', 'placeholder': ('Twitter url. e.g. http://www.twitter.com/sirneij')}))
    facebook_url = forms.CharField(widget=forms.TextInput(attrs={'class':'full-width', 'placeholder': ('Facebook url. e.g. http://www.facebook.com/sirneij')}))
    linkedin_url = forms.CharField(widget=forms.TextInput(attrs={'class':'full-width', 'placeholder': ('Linkedin url. e.g. http://www.linkedin.com/sirneij')}))
    github_url = forms.CharField(widget=forms.TextInput(attrs={'class':'full-width', 'placeholder': ('Github url. e.g. http://www.github.com/sirneij')}))
    codepen_url = forms.CharField(widget=forms.TextInput(attrs={'class':'full-width', 'placeholder': ('Codepen url. e.g. http://www.codepen.com/sirneij')}))
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'profile_pics', 'bio', 'phone_number', 'twitter_url', 'facebook_url', 'linkedin_url', 'github_url', 'codepen_url',)
