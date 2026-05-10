from django.db import models
from django.db.models import ForeignKey


class Tag(models.Model):
    name = models.CharField(max_length=25, verbose_name='Тег')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self) -> str:
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(
        Tag,
        through='Scope',
        related_name='articles',
        verbose_name='Теги',
    )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title



class Scope(models.Model):
    article = ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='scopes',
        verbose_name='Статья',
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        verbose_name='Тег',
    )
    is_main = models.BooleanField(
        default=False,
        verbose_name='Основной',

    )
    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['-is_main', 'tag__name']

    def __str__(self):
        return f'{self.article} | {self.tag}'

