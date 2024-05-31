from django.db import models
from django.contrib.auth.models import User

# Modèle pour les QR Codes


class QRCode(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='qrcodes')
    lien = models.URLField()
    date_creation = models.DateTimeField(auto_now_add=True)
    actif = models.BooleanField(default=True)


# Modèle pour l'historique des scans
class HistoriqueScan(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='historique_scans')
    qrcode = models.ForeignKey(QRCode, on_delete=models.CASCADE, related_name='scans')
    date_scan = models.DateTimeField(auto_now_add=True)
    device = models.CharField(max_length=255)


# Modèle pour l'historique des QR codes partagés entre amis
class PartageQR(models.Model):
    qrcode = models.ForeignKey(QRCode, on_delete=models.CASCADE, related_name='partages')
    utilisateur_source = models.ForeignKey(User, on_delete=models.CASCADE, related_name='partages_envoyes')
    utilisateur_cible = models.ForeignKey(User, on_delete=models.CASCADE, related_name='partages_recus')
    date_partage = models.DateTimeField(auto_now_add=True)
