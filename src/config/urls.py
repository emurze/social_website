from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include, reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect(reverse_lazy('account:dashboard'))),
    path('account/', include('apps.account.urls', namespace='account')),
]
