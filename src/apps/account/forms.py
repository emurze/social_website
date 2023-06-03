from django import forms
from django.contrib.auth.models import User

from apps.account.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password1']:
            raise forms.ValidationError('Passwords must be the same')
        return cd['password2']

    def clean_email(self):
        cd = self.cleaned_data
        if User.objects.filter(email=cd["email"]).exists():
            raise forms.ValidationError('Email already in use.')
        return cd["email"]


class UserEditorForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def clean_email(self):
        cd = self.cleaned_data
        other_users = User.objects.exclude(id=self.instance.id)
        if other_users.filter(email=cd["email"]).exists():
            raise forms.ValidationError('Email already in use.')
        return cd["email"]


class ProfileEditorForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
