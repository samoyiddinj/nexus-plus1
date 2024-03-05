from django.shortcuts import render
from .models import Category
from nexus.product.models import Product, ProductImage
from nexus.geo.models import City
from nexus.product import services


def index(request):
    cities = City.objects.all()
    categories = Category.objects.filter(parent_id=None)
    categoriess = Category.objects.all()
    if request.GET.get('city') or request.GET.get('category'):
        products = services.get_latest_products(request.GET.get('city'))
    else:
        products = services.get_latest_products(6)
        ctx = {
            "categories": categories,
            "categoriess": categoriess,
            "cities": cities,
            "products": products
        }
        return render(request, 'category.html', ctx)