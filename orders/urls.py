from django.urls import path

from . import views


urlpatterns = [

    path(

        'order/<int:product_id>/',

        views.order_product,

        name='order_product'

    ),
    path('order-success/<int:order_id>', views.order_success, name='order_success'),
    path('pay/<int:order_id>/', views.initiate_payment, name='initiate_payment'),

    path('payment/callback/', views.payment_callback, name='payment_callback'),
    

]