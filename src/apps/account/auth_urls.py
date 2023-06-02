from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

urlpatterns = [
    # ALL THE SAME LOGIC IN AUTH URLS
    # path('', include('django.contrib.auth.urls')),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Change password
    path(
        'password-change/',
        auth_views.PasswordChangeView.as_view(
            success_url=reverse_lazy('account:password_change_done'),
        ),
        name='password_change',
    ),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    # Email-form / done. Send link with token and uid on email.
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            success_url=reverse_lazy('account:password_reset_done')
        ),
        name='password_reset',
    ),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),

    # Check uid and token then reset-form / done.
    path(
        'password-reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            success_url=reverse_lazy('account:password_reset_complete')
        ),
        name='password_reset_confirm',
    ),
    path(
        'password_reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),
]
