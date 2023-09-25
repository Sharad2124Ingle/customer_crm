
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/', views.update_record, name='update_record'),
    
]