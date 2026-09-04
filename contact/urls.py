from django.urls import path

from . import views

app_name = 'contact'

urlpatterns = [

    path(
        '',
        views.contact_page,
        name='contact_page'
    ),

    path(
        'consultation/',
        views.consultation_page,
        name='consultation_page'
    ),

]