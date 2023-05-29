from django.contrib import admin

from .models import Category, Product, Commande

# Register your models here.
admin.site.site_header = "Admin TI-Varotra"
admin.site.site_title = "Gestion Adminstrateur de TI-Varotra"
admin.site.index_title = "Manageur"


class AdminCategorie(admin.ModelAdmin):
    list_display = ('name', 'date_added')


class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added')
    search_fields = ('title',)
    list_editable = ('price', 'category')


class AdminCommande(admin.ModelAdmin):
    list_display = ('items', 'name', 'email', 'adresse',
                    'pays', 'ville', 'total', 'date_commande')


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategorie)
admin.site.register(Commande, AdminCommande)
