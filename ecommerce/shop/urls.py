from django.urls import path

from shop.views import index, product, detail, checkout, confirmation

urlpatterns = [
    path('', index, name='home'),
    path('shop', product, name='product'),
    path('shop/<int:myid>', detail, name='detail'),
    path('shop/checkout', checkout, name='checkout'),
    path('shop/confirmation', confirmation, name='confirmation')
]