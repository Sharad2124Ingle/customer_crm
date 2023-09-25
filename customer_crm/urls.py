
from django.contrib import admin
from django.urls import path, include
from qrcodeapp import views as qrcodeapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('accounts/', include('accounts.urls')),
    path('qrcodeapp/', include('qrcodeapp.urls')),
    path('select_record/', qrcodeapp_views.select_record, name='select_record'),
    path('client/', include('client.urls')),
    path('offerapp/', include('offerapp.urls')),
]
