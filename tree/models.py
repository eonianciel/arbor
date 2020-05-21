from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    initials = models.CharField(max_length=500, db_index=True, verbose_name='ФИО')
    dates = models.CharField(max_length=350, db_index=True, verbose_name='Даты')
    bio = models.TextField(blank=True, db_index=True, verbose_name='Биография')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Слаг')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.initials
