from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

urlpatterns = [
    # Registration
    path('register_client/', views.retail_user_registration, name='retail_user_registration'),
    path('login_client/',  views.login_client, name='login_client'),
    path('logout_client/', auth_views.LogoutView.as_view(), name='logout_client'),
]


"""

urlpatterns = [
    # Registration
    path('register/', views.retail_user_registration, name='retail_user_registration'),

    # Login and Logout
    path('login/', auth_views.LoginView.as_view(template_name='registration/retail_user_login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

 path('login/local/', auth_views.LoginView.as_view(template_name='registration/local_user_login.html'), name='login_local')

path('register_client/', views.retail_user_registration, name='retail_user_registration'),
    path('login_client/', views.login_client, name='login_client'),
    path('logout_client/', views.logout_client, name='logout_client'),

"""