from django.db import models

# Create your models here.

class Testimonial(models.Model):

    RATING_CHOICES = (

        (1, '1 Star'),

        (2, '2 Stars'),

        (3, '3 Stars'),

        (4, '4 Stars'),

        (5, '5 Stars'),

    )

    name = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=100,
        blank=True
    )

    testimonial = models.TextField()

    rating = models.IntegerField(
        choices=RATING_CHOICES,
        default=5
    )

    featured = models.BooleanField(
        default=False
    )

    approved = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name