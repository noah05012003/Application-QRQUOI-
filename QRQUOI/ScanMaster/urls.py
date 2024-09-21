#ScanMaster/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('generate_qrcode/', views.generate_qrcode, name='generate_qrcode'),
    path('historique_qrcodes/', views.historique_qrcodes, name='historique_qrcodes'),
    path('', views.index, name='index'),
]