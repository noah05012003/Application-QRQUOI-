import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "doclist.settings")
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

# Modèle pour la table 'Utilisateur'
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Les utilisateurs doivent avoir une adresse email valide.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser doit avoir is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser doit avoir is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class Utilisateur(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    nom = models.CharField(max_length=255)
    date_inscription = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Liste des champs obligatoires lors de la création d'un superuser, en dehors de l'email et du mot de passe

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


