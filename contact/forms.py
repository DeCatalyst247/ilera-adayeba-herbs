from django import forms
from .models import (
    ContactMessage,
    ConsultationRequest
)

class ContactForm(forms.ModelForm):

    class Meta:

        model = ContactMessage

        fields = [
            'name',
            'email',
            'phone',
            'subject',
            'message'
        ]

class ConsultationForm(forms.ModelForm):

    class Meta:

        model = ConsultationRequest

        fields = [
            'name',
            'email',
            'phone',
            'concern'
        ]