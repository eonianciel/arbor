from django.db import models
from django.conf import settings
from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
    related_name='images_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=350)
    slug = models.SlugField(max_length=150, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.initials)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('image_create', kwargs={'slug':self.slug})
