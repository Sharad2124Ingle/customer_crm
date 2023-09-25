from django.urls import path
from . import views

urlpatterns = [
    path('offers/', views.offer_list, name='offer_list'),
    path('redeem/<int:offer_id>/', views.redeem_offer, name='redeem_offer'),
    path('offer/<int:offer_id>/', views.offer_details, name='offer_details'),
    #path('retailqr/', views.retailqr, name='retailqr'),
    #path('offer/confirmation/', views.offer_confirmation, name='offer_confirmation'),
    #path('generate_code/', views.generate_qr_code, name='generate_qr'),
    path('generate_code/<int:offer_id>/', views.generate_qr_code, name='generate_qr'),
    #path('generate_shop_qr_code/<int:offer_id>/', views.generate_shop_qr_code, name='generate_shop_qr_code'),
]
