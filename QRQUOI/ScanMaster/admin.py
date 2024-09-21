from django.contrib import admin
from .models import Utilisateur, QRCode, HistoriqueScan, PartageQR

admin.site.register(Utilisateur)
admin.site.register(QRCode)
admin.site.register(HistoriqueScan)
admin.site.register(PartageQR)
