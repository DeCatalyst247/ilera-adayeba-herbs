# Create your views here.
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
import requests

from products.models import Product
from django.contrib import messages
from .forms import OrderForm
from django.conf import settings
from .models import Order
from orders.models import Order
from django.urls import reverse


def order_product(
    request,
    product_id
):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    if request.method == 'POST':

        form = OrderForm(
            request.POST
        )

        if form.is_valid():

            order = form.save(
                commit=False
            )

            order.product = product

            order.save()

            return redirect('order_success', order_id=order.id)

    else:

        form = OrderForm()

    return render(

        request,

        'orders/order_form.html',

        {

            'form': form,

            'product': product

        }

    )

def order_success(request,order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/success.html',{'order':order})

'''def initiate_payment(request, order_id):

    order = Order.objects.get(id=order_id)

    url = "https://api.paystack.co/transaction/initialize"

    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "email": order.email,
        "amount": int(order.product.price * order.quantity) * 100,  # convert to kobo
        "reference": str(order.id),
        "callback_url": request.build_absolute_uri("/payment/callback/")
    }

    response = requests.post(url, json=data, headers=headers)

    res = response.json()

    if res["status"]:

        return redirect(res["data"]["authorization_url"])

    return redirect("order_success", order_id=order.id)'''


'''def initiate_payment(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id
    )

    url = "https://api.paystack.co/transaction/initialize"

    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "email": order.email,
        "amount": int(order.product.price * order.quantity * 100),
        "reference": str(order.id),
        "callback_url": request.build_absolute_uri(
            "/payment/callback/"
        ),
    }

    try:

        response = requests.post(
            url,
            json=data,
            headers=headers,
            timeout=30
        )

        print("PAYSTACK STATUS CODE:", response.status_code)
        print("PAYSTACK RESPONSE:", response.text)

        response.raise_for_status()

        res = response.json()

        if res.get("status"):

            return redirect(
                res["data"]["authorization_url"]
            )

        messages.error(
            request,
            "Paystack could not initialize the payment."
        )

        return redirect(
            "order_success",
            order_id=order.id
        )

    except requests.exceptions.RequestException as e:

        print("PAYSTACK REQUEST ERROR:", e)

        messages.error(
            request,
            "Unable to connect to Paystack. Please try again."
        )

        return redirect(
            "order_success",
            order_id=order.id
        )'''


'''def initiate_payment(request, order_id):

    order = get_object_or_404(Order, id=order_id)

    url = "https://api.paystack.co/transaction/initialize"

    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "email": order.email,
        "amount": int(order.product.price * order.quantity * 100),
        "reference": f"ILERA-{order.id}",
        order.payment_reference =reference.order.save(update_fields=["payent_reference"])
        "callback_url": request.build_absolute_uri(
    reverse("payment_callback")
),
    }

    try:

        response = requests.post(
            url,
            json=data,
            headers=headers,
            timeout=15
        )

        print("PAYSTACK STATUS CODE:", response.status_code)
        print("PAYSTACK RESPONSE:", response.text)

        response.raise_for_status()

        res = response.json()

        if res.get("status"):

            authorization_url = res["data"]["authorization_url"]

            return redirect(authorization_url)

        print("PAYSTACK ERROR:", res)

        messages.error(
            request,
            "Unable to connect to Paystack. Please try again."
        )

        return redirect(
            "order_success",
            order_id=order.id
        )

    except requests.exceptions.RequestException as e:

        print("PAYSTACK CONNECTION ERROR:", e)

        messages.error(
            request,
            "Unable to connect to Paystack. Please try again."
        )

        return redirect(
            "order_success",
            order_id=order.id
        )
'''


def initiate_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    # Create a unique reference for this order
    reference = f"ILERA-{order.id}"

    # Save the Paystack reference to the order
    order.payment_reference = reference
    order.save(update_fields=["payment_reference"])

    url = "https://api.paystack.co/transaction/initialize"

    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "email": order.email,
        "amount": int(order.product.price * order.quantity * 100),
        "reference": reference,
        "callback_url": request.build_absolute_uri(
            reverse("payment_callback")
        ),
    }

    try:
        response = requests.post(
            url,
            json=data,
            headers=headers,
            timeout=15,
        )

        print("PAYSTACK STATUS CODE:", response.status_code)
        print("PAYSTACK RESPONSE:", response.text)

        if response.status_code != 200:
            messages.error(
                request,
                "Unable to connect to Paystack. Please try again."
            )
            return redirect(
                "order_success",
                order_id=order.id
            )

        res = response.json()

        if res.get("status"):
            authorization_url = res["data"]["authorization_url"]

            return redirect(authorization_url)

        print("PAYSTACK ERROR:", res)

        messages.error(
            request,
            "Unable to connect to Paystack. Please try again."
        )

        return redirect(
            "order_success",
            order_id=order.id
        )

    except requests.exceptions.Timeout:
        print("PAYSTACK ERROR: Request timed out")

        messages.error(
            request,
            "Paystack took too long to respond. Please try again."
        )

        return redirect(
            "order_success",
            order_id=order.id
        )

    except requests.exceptions.ConnectionError as e:
        print("PAYSTACK CONNECTION ERROR:", e)

        messages.error(
            request,
            "Unable to connect to Paystack. Please try again."
        )

        return redirect(
            "order_success",
            order_id=order.id
        )

    except requests.exceptions.RequestException as e:
        print("PAYSTACK REQUEST ERROR:", e)

        messages.error(
            request,
            "Unable to process payment. Please try again."
        )

        return redirect(
            "order_success",
            order_id=order.id
        )


def payment_callback(request):

    reference = request.GET.get("reference")

    url = f"https://api.paystack.co/transaction/verify/{reference}"

    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"
    }

    response = requests.get(url, headers=headers)

    res = response.json()

    if res["data"]["status"] == "success":

        order = Order.objects.get(payment_reference=reference)
        order.payment_status = True
        order.status = "paid"
        order.payment_reference = reference
        order.save()

        return redirect("order_success",order_id=order.id)

    return redirect("order_failed")




