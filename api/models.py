from django.db import models

from django.conf import settings

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles_api')
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
