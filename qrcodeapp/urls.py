from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name = 'qrcodeapp'

urlpatterns = [
    path('select_record/', views.select_record, name='select_record'),
    path('generate_qr_code/<int:record_id>/', views.generate_qr_code, name='generate_qr_code'),
    path('auto_refresh/<int:record_id>/', views.auto_refresh_view, name='auto_refresh'),
     
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




