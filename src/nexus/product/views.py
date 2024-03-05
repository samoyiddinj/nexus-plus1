from django.shortcuts import render, redirect
from nexus.category.models import Category
from .models import Product, ProductImage
from .services import get_latest_products
from .models import City
from . import services
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


def index(request):
    cities = City.objects.all()
    categories = Category.objects.filter(parent_id=None)
    categoriess = Category.objects.all()
    # products = Product.objects.all().select_related('category', 'city', 'user')
    products = services.get_latest_products(3)
    print(products)

    ctx = {
        "categories": categories,
        "categoriess": categoriess,
        "cities": cities,
        "products": products
    }

    return render(request, 'index.html', ctx)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect("item:detail", item.id)
    else:
        form = ProductForm(None)
    context = {
        "form": form
    }

    return render(request, 'post_ad.html', context)


def detail_product(request):
    return render(request, 'ad_detail.html', {})
