# Create your views here.
from django.shortcuts import (
    render,
    redirect
)

from django.contrib import messages

from .forms import (
    ContactForm,
    ConsultationForm
)


def contact_page(request):

    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Your message has been sent successfully.'
            )

            return redirect(
                'contact:contact_page'
            )

    else:

        form = ContactForm()

    context = {
        'form': form
    }

    return render(
        request,
        'contact/contact.html',
        context
    )

def consultation_page(request):

    if request.method == 'POST':

        form = ConsultationForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Consultation request submitted successfully.'
            )

            return redirect(
                'contact:consultation_page'
            )

    else:

        form = ConsultationForm()

    context = {
        'form': form
    }

    return render(
        request,
        'contact/consultation.html',
        context
    )