import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "doclist.settings")
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

# Modèle pour la table 'Utilisateur'
class Utilisateur(AbstractBaseUser):
    nom = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=255, unique=True, null=False)
    #password = models.CharField(max_length=255, null=False) est deja config car vient de 'AbstractBaseUser'
    DateInscription = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'   #détermine quel champ du modèle utilisateur est utilisé comme identifiant pour l'authentification
    REQUIRED_FIELDS = ['nom']  #Pour la création du superutilisatuer

    class Meta:
        app_label = 'QRQUOI'

    def __str__(self):
        return self.email

# Modèle pour la table 'QRcode'
class QRCode(models.Model):
    utilisateur_qrcode = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='qrcodes', null=True)
    lien = models.URLField(null=True)
    date_creation = models.DateTimeField(default= timezone.now)
    actif = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.lien} - {'Actif' if self.actif else 'Inactif'}"

class HistoriqueScan(models.Model):
    utilisateur_historique = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='historique_scan',null=True )
    qrcode = models.ForeignKey(QRCode, on_delete=models.CASCADE, related_name='scans')
    date_scan = models.DateTimeField(auto_now_add=True)
    device = models.CharField(max_length=255)

    def __str__(self):
        return f"Scan de {self.qrcode.lien} par {self.utilisateur.nom} le {self.date_scan}"

class PartageQR(models.Model):
    qrcode = models.ForeignKey(QRCode, on_delete=models.CASCADE, related_name='partages')
    utilisateur_source = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='partages_envoyes',null=True)
    utilisateur_cible = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='partages_recus',null=True)
    date_partage = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Partagé de {self.utilisateur_source.nom} à {self.utilisateur_cible.nom} le {self.date_partage}"


#test01commit



