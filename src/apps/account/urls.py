from django.urls import path, include

from .views import dashboard, UserRegistrationView

app_name = 'account'

urlpatterns = [
    path('', include('apps.account.auth_urls')),
    path('', dashboard, name='dashboard'),
    path('register/', UserRegistrationView.as_view(), name='register'),
]
