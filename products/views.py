# Create your views here.
from django.shortcuts import (
    render,
    get_object_or_404
)

from .models import Product,Category
from django.db.models import Q

def product_list(request):

    products = Product.objects.all()

    query = request.GET.get(
        'q'
    )

    if query:

        products = products.filter(

            Q(name__icontains=query)

            |

            Q(description__icontains=query)

        )

    context = {

        'products': products

    }

    return render(
        request,
        'products/product_list.html',
        context
    )



def product_detail(request, slug):

    product = get_object_or_404(
        Product,
        slug=slug
    )

    context = {
        'product': product
    }

    return render(
        request,
        'products/product_detail.html',
        context
    )


def category_products(
    request,
    slug
):

    category = Category.objects.get(
        slug=slug
    )

    products = Product.objects.filter(
        category=category
    )

    context = {
        'category': category,
        'products': products
    }

    return render(
        request,
        'products/category_products.html',
        context
    )