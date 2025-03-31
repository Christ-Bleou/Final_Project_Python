from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Modèle utilisateur
class Utilisateur(AbstractUser):
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('artiste', 'Artiste'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')
    date_inscription = models.DateTimeField(auto_now_add=True)

    # Remplacez les groupes par un nom associé unique.
    groups = models.ManyToManyField(
        Group,
        related_name="ecommerce_utilisateur_set",  # Nouvel accesseur inverse unique.
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups"
    )
    # Remplacez les autorisations utilisateur par un nom associé unique.
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="ecommerce_utilisateur_permissions_set",  # Nouvel accesseur inverse unique.
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions"
    )

# Modèle Oeuvre
class Oeuvre(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    artiste = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='oeuvres')
    prix_location = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    image = models.ImageField(upload_to='oeuvres/')
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

# Modèle Location
class Location(models.Model):
    client = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='locations')
    oeuvre = models.ForeignKey(Oeuvre, on_delete=models.CASCADE, related_name='locations')
    date_debut = models.DateField()
    date_fin = models.DateField()
    statut = models.CharField(max_length=20, choices=[('en cours', 'En cours'), ('terminée', 'Terminée')], default='en cours')

    def __str__(self):
        return f"Location de {self.oeuvre.titre} par {self.client.username}"

# Modèle Paiement
class Paiement(models.Model):
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    statut = models.CharField(max_length=20, choices=[('en attente', 'En attente'), ('payé', 'Payé'), ('annulé', 'Annulé')], default='en attente')
    date_paiement = models.DateTimeField(auto_now_add=True)


