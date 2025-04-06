from django.test import TestCase
# Explicitation
from core.models import Article
from django.contrib.auth.models import User

class CoreTest(TestCase):
    def test_creation_article(self):
        auteur = User.objects.create(username='admin')
        article = Article.objects.create(titre='Test', contenu='Texte', auteur=auteur)
        self.assertEqual(str(article), 'Test')
