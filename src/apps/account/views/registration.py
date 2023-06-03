from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from apps.account.forms import LoginForm, UserRegistrationForm
from apps.account.models import Profile


class LoginView(View):
    title = 'Login'
    template_name = 'registration/login.html'

    @login_required
    def get(self, request: WSGIRequest) -> HttpResponse:
        context = {
            'title': self.title,
            'form': LoginForm(),
        }
        return render(request, self.template_name, context)

    @login_required
    def post(self, request: WSGIRequest) -> HttpResponse:
        if (form := LoginForm(request.POST)).is_valid():
            cd = form.cleaned_data
            user: User | None = authenticate(request, username=cd["username"],
                                             password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled user')
            else:
                return HttpResponse('Invalid login')

        context = {
            'title': self.title,
            'form': form,
        }
        return render(request, self.template_name, context)


class UserRegistrationView(View):
    register_title = 'Registration'
    register_template_name = 'account/register.html'
    done_title = 'Welcome'
    done_template_name = 'account/register_done.html'

    def get(self, request: WSGIRequest) -> HttpResponse:
        context = {
            'title': self.register_title,
            'form': UserRegistrationForm(),
        }
        return render(request, self.register_template_name, context)

    def post(self, request: WSGIRequest) -> HttpResponse:
        if (form := UserRegistrationForm(request.POST)).is_valid():
            cd = form.cleaned_data
            user = form.save(commit=False)
            user.set_password(cd['password1'])
            user.save()
            Profile.objects.create(user=user)

            context = {
                'title': self.done_title,
                'new_user': user,
            }
            return render(request, self.done_template_name, context)
        else:
            context = {
                'title': self.register_title,
                'form': form,
            }
            return render(request, self.register_template_name, context)
