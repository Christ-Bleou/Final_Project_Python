from django.test import TestCase
# Explicitation
from ecommerce.models import Oeuvre, Utilisateur, Article
from django.contrib.auth.models import User

class EcommerceTest(TestCase):
    def test_creation_article(self):
        auteur = User.objects.create(username='admin')
        article = Article.objects.create(titre='Test', contenu='Texte', auteur=auteur)
        self.assertEqual(str(article), 'Test')

class OeuvreModelTest(TestCase):
    def test_str(self):
        user = Utilisateur.objects.create(username="artiste")
        oeuvre = Oeuvre.objects.create(titre="Mona Lisa", description="Portrait", artiste=user, prix_location=100)
        self.assertEqual(str(oeuvre), "Mona Lisa")