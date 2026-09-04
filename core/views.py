from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from products.services import(get_featured_products)
from blog.models import BlogPost

from testimonials.services import (
    get_featured_testimonials
)
def home(request):

    featured_products = get_featured_products()
    latest_posts = BlogPost.objects.filter(published=True
            )[:3]
    featured_testimonials = (
    get_featured_testimonials()
)

    context = {

        'featured_products':
        featured_products,
        'latest_posts' :
        latest_posts,
        'featured_testimonials':
        featured_testimonials

    }

    return render(
        request,
        'core/home.html',
        context
    )


def robots_txt(request):

    lines = [

        "User-agent: *",

        "Allow: /"

    ]

    return HttpResponse(

        "\n".join(lines),

        content_type="text/plain"

    )