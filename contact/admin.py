from django.contrib import admin

# Register your models here.
from .models import (
    ContactMessage,
    ConsultationRequest
)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'subject',
        'is_read',
        'replied',
        'created_at'
    )

    search_fields = (
        'name',
        'email',
        'subject'
    )

@admin.register(ConsultationRequest)
class ConsultationRequestAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'phone',
        'status',
        'is_read',
        'preferred_contact_method',
        'created_at'
    )

    search_fields = (
        'name',
        'email'
    )