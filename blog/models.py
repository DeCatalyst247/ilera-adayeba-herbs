from django.db import models

# Create your models here.
from django.utils.text import slugify






class BlogCategory(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class BlogPost(models.Model):

    category = models.ForeignKey(
        BlogCategory,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    title = models.CharField(
        max_length=255
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    image = models.ImageField(
        upload_to='blog/'
    )

    content = models.TextField()

    published = models.BooleanField(
        default=True
    )
    featured = models.BooleanField(
        default = False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title