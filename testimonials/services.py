from .models import Testimonial

def get_featured_testimonials():

    return Testimonial.objects.filter(

        featured=True,

        approved=True

    )[:6]