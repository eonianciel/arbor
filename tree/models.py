from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_index=True, null=True)
    initials = models.CharField(max_length=500, db_index=True, verbose_name='ФИО')
    dates = models.CharField(max_length=350, db_index=True, verbose_name='Даты')
    bio = models.TextField(blank=True, db_index=True, verbose_name='Биография')
    slug = models.SlugField(max_length=50, blank=True, unique=True)
    image = models.ImageField(blank=True, upload_to='posts', verbose_name='Фото')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    famille = models.ManyToManyField('Famille', blank=True, related_name='posts', verbose_name='Род')

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.initials)
        super().save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.initials

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('post_edit', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-published_date']


class Famille(models.Model):
    title = models.CharField(max_length=250, verbose_name='Фамилия')
    details = models.TextField(blank=True, db_index=True, verbose_name='Подробности')
    slug = models.SlugField(max_length=50, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('famille_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('famille_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('famille_delete', kwargs={'slug': self.slug})
