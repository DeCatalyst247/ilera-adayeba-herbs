from django.shortcuts import render

# Create your views here.
from django.shortcuts import (
    redirect
)

from .forms import SubscriberForm


def subscribe(request):

    if request.method == "POST":

        form = SubscriberForm(
            request.POST
        )

        if form.is_valid():

            form.save()

    return redirect('/')