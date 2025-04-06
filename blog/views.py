from django.shortcuts import render, get_object_or_404
# Explicitation
from blog.models import Article

def liste_articles(request):
    articles = Article.objects.order_by('-date_publication')
    return render(request, 'blog/liste_articles.html', {'articles': articles})

def detail_article(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/detail_article.html', {'article': article})
