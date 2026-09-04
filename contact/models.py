from django.db import models

# Create your models here.




class ContactMessage(models.Model):

    name = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    subject = models.CharField(
        max_length=200
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    is_read = models.BooleanField(default=False)
    replied = models.BooleanField(default=False)

    def __str__(self):
        return self.name



class ConsultationRequest(models.Model):

    name = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=20
    )

    concern = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('contacted', 'Contacted'),
            ('completed', 'Completed'),
        ],
        default='pending'
    )

    is_read = models.BooleanField(
    default=False
    )
    preferred_contact_method = models.CharField(
        max_length=20,
        choices=[
            ('phone', 'Phone'),
            ('whatsapp', 'WhatsApp'),
            ('email', 'Email'),
        ],
        default='whatsapp'
    )
    def __str__(self):
        return self.name