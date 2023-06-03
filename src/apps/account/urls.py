from django.conf import settings
from django.urls import path, include

from .views import dashboard, UserRegistrationView, ProfileEditView

app_name = 'account'

urlpatterns = [
    path('', include('apps.account.auth_urls')),
    path('', dashboard, name='dashboard'),
    path('edit/', ProfileEditView.as_view(), name='edit'),
    path('register/', UserRegistrationView.as_view(), name='register'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document=settings.MEDIA_ROOT)
