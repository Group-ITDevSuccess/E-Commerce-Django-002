from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Product, Commande

# Create your views here.


def index(request):
    product_object = Product.objects.all()
    item_name = request.GET.get('item-name')
    if (item_name != "" and item_name is not None):
        product_object = Product.objects.filter(title__icontains=item_name)

    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    context = {
        'products': product_object
    }
    return render(request, 'shop/index.html', context)


def detail(request, myid):
    product = Product.objects.get(id=myid)

    context = {
        'product': product
    }

    return render(request, 'shop/detail.html', context)


def checkout(request):
    if (request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        adresse = request.POST.get('adresse')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        ville = request.POST.get('ville')
        zipcode = request.POST.get('zipcode')
        commande = Commande(
            name=name, email=email, ville=ville,
            adresse=adresse,  pays=pays, zipcode=zipcode)
        commande.save()

    return render(request, 'shop/checkout.html')
