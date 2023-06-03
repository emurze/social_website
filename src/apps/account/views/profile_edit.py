from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib import messages

from apps.account.forms import UserEditorForm, ProfileEditorForm


class ProfileEditView(View):
    title = 'Edit the profile'
    template_name = 'account/edit.html'

    def get(self, request: WSGIRequest) -> HttpResponse:
        context = {
            'title': self.title,
            'user_form': UserEditorForm(),
            'profile_form': ProfileEditorForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request: WSGIRequest) -> HttpResponse:
        user_form = UserEditorForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditorForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES
        )
        if profile_form.is_valid() & user_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect(reverse('account:dashboard'))
        else:
            messages.error(request, 'Error updating your profile')
            context = {
                'title': self.title,
                'user_form': user_form,
                'profile_form': profile_form,
            }
            return render(request, self.template_name, context)
