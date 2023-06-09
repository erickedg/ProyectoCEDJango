from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)  # la url
    published = models.BooleanField(default=False)

    def __str__(self):  # en los desplegables del post, aparecera esto
        return self.title
