# accounts/urls.py
from django.urls import path
from . import views
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
#from whatsotp.views import mobiotp, motp

urlpatterns = [
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    #path('change_password/<str:token>/', views.change_password, name='change_password'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt',
        success_url=reverse_lazy('password_reset_done')
    ), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html',
        success_url=reverse_lazy('password_reset_complete')
    ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ), name='password_reset_complete'),
    path('login_with_otp/', views.login_with_otp, name = 'login_with_otp'),
    path('otp_verification/', views.otp_verification, name='otp_verification'),
    path('mobiotp/', views.mobileotp, name='mobiotp'),
    path('sha_011_01_rli_2023/', views.whatsapp_webhook, name='whatsapp_webhook')
]



#http://192.168.0.142:8000/accounts/sha_011_01_rli_2023/
#token : sharad_is_awesome
