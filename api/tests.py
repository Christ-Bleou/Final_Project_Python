from django.test import TestCase
from api.models import Article
from django.contrib.auth.models import User

class ApiTest(TestCase):
    def test_creation_article(self):
        auteur = User.objects.create(username='admin')
        article = Article.objects.create(titre='Test', contenu='Texte', auteur=auteur)
        self.assertEqual(str(article), 'Test')
