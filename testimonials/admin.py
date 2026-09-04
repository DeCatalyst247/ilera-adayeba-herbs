from django.contrib import admin

# Register your models here.
from .models import Testimonial



@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = (

        'name',

        'rating',

        'featured',

        'approved',

        'created_at'

    )

    list_filter = (

        'rating',

        'featured',

        'approved'

    )

    search_fields = (

        'name',

        'testimonial'

    )