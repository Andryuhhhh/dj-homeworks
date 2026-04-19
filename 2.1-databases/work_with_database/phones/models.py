from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    id = models.AutoField(primary_key=True)  # можно не указывать, Django создаст сам
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.URLField(default='')  # или CharField, если ссылки на картинки
    release_date = models.DateField(null=True, blank=True)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name