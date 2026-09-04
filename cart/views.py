# Create your views here.
from django.shortcuts import (
    redirect,
    render,
    get_object_or_404
)
from orders.forms import OrderForm
from products.models import Product
from django.contrib import messages
from orders.models import Order,OrderItem

def add_to_cart(
    request,
    product_id
):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    cart = request.session.get(
        'cart',
        {}
    )

    if str(product_id) in cart:

        cart[str(product_id)] += 1

    else:

        cart[str(product_id)] = 1

    request.session['cart'] = cart

    return redirect(
        'cart_detail'
    )

def remove_from_cart(
    request,
    product_id
):

    cart = request.session.get(
        'cart',
        {}
    )

    if str(product_id) in cart:

        del cart[str(product_id)]

    request.session['cart'] = cart

    return redirect(
        'cart_detail'
    )

def cart_detail(request):

    cart = request.session.get(
        'cart',
        {}
    )

    items = []

    total = 0

    for product_id, quantity in cart.items():

        product = Product.objects.get(
            id=product_id
        )

        subtotal = (
            product.price * quantity
        )

        total += subtotal

        items.append({

            'product': product,

            'quantity': quantity,

            'subtotal': subtotal

        })

    return render(

        request,

        'cart/cart_detail.html',

        {

            'items': items,

            'total': total

        }

    )



'''def checkout(request):

    cart = request.session.get("cart", {})

    if not cart:
        messages.warning(request, "Your cart is empty.")
        return redirect("cart_detail")

    items = []
    total = 0

    for product_id, quantity in cart.items():

        product = get_object_or_404(Product, id=product_id)

        subtotal = product.price * quantity

        total += subtotal

        items.append({
            "product": product,
            "quantity": quantity,
            "subtotal": subtotal,
        })

    if request.method == "POST":

        form = OrderForm(request.POST)

        if form.is_valid():

            # For now, create one order using the first product
           # first_item = items[0]

            order = form.save(commit=False)

            order.product = item[0]["product"]
            order.quantity = 1

            order.save()
            for item in items:
                OrderItem.objects.create(
                    order=order,
    product=item["product"],
    quantity=item["quantity"],
    price=item["product"].price,
                )

            # Clear cart
            request.session["cart"] = {}

            return redirect("initiate_payment", order_id=order.id)

    else:

        form = OrderForm()

    return render(
        request,
        "orders/checkout.html",
        {
            "form": form,
            "items": items,
            "total": total,
        },
    )
    '''

def checkout(request):

    cart = request.session.get('cart', {})

    items = []
    total = 0

    # Get products from cart
    for product_id, quantity in cart.items():

        product = get_object_or_404(
            Product,
            id=product_id
        )

        subtotal = product.price * quantity

        total += subtotal

        items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    # Prevent checkout with an empty cart
    if not items:
        return redirect('cart_detail')

    if request.method == "POST":

        form = OrderForm(request.POST)

        if form.is_valid():

            # Create the order
            order = form.save(commit=False)

            # For the moment, save the first product
            # We will replace this with OrderItem for true
            # multi-product orders.
            first_item = items[0]

            order.product = first_item['product']
            order.quantity = first_item['quantity']

            order.save()

            # Clear cart
            request.session['cart'] = {}

            # Go to Paystack
            return redirect("initiate_payment", order_id=order.id)
            

    else:

        form = OrderForm()

    return render(
        request,
        "orders/checkout.html",
        {
            "form": form,
            "items": items,
            "total": total,
        }
    )