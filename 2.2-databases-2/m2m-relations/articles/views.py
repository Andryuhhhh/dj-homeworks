from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    # Получаем все статьи, отсортированные по дате публикации (новые сверху)
    articles = Article.objects.order_by(ordering)

    context = {
        'object_list': articles,
    }

    return render(request, template, context)
