from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name='reset_password'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>', 
        auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name='password_reset_complete'),
]