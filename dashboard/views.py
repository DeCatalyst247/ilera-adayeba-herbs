# Create your views here.
from django.shortcuts import render
from django.contrib.admin.views.decorators import(
    staff_member_required
)
from products.models import(
    Product,Category)
from blog.models import BlogPost
from contact.models import (
    ContactMessage,
    ConsultationRequest
)
from testimonials.models import Testimonial



@staff_member_required
def admin_dashboard(request):

    total_products = Product.objects.count()

    total_posts = BlogPost.objects.count()

    total_messages = ContactMessage.objects.count()

    total_consultations = (
        ConsultationRequest.objects.count()
    )

    total_testimonials = (
        Testimonial.objects.count()
    )
    recent_messages = ContactMessage.objects.order_by(
        '-created_at'
    )[:5]
    recent_textimonials =Testimonial.objects.order_by(
        '-created_at'
    )[:5]

    recent_consultations = ConsultationRequest.objects.order_by(
        '-created_at'
    )[:5]

    categories = Category.objects.all()

    category_names = []

    category_counts = []
    for category in categories:

        category_names.append(
            category.name
        )

        category_counts.append(

            Product.objects.filter(
                category=category
            ).count()

        )


    context = {

        'total_products':
        total_products,

        'total_posts':
        total_posts,

        'total_messages':
        total_messages,

        'total_consultations':
        total_consultations,

        'total_testimonials':
        total_testimonials,

        'recent_messages':
         recent_messages,

        'recent_consultations':
        recent_consultations,

        'category_names':
        category_names,
        
        'category_counts':
        category_counts

    }

    return render(
        request,
        'dashboard/dashboard.html',
        context
    )