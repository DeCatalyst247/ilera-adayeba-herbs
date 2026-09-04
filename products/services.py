from .models import Product


def get_featured_products():

    return Product.objects.filter(
        featured=True
    )


def get_all_products():

    return Product.objects.select_related(
        'category'
    )