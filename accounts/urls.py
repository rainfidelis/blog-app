from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset_form.html"), name='reset_password'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name='password_reset_done'),
    path(r'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
        auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name='password_reset_complete'),
]