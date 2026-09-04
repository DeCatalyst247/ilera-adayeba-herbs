from django import forms
from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:

        model = Order

        fields = [
            "customer_name",
            "email",
            "phone",
            "address",
            "order_note",
        ]

        widgets = {

            "address": forms.Textarea(
                attrs={
                    "rows":3
                }
            ),

            "order_note": forms.Textarea(
                attrs={
                    "rows":3
                }
            )
        }