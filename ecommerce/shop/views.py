from django.shortcuts import render

from .models import Product

# Create your views here.
def index(request):
    product_object = Product.objects.all()
    context = {
        'products': product_object
    }
    return render(request, 'shop/index.html', context)