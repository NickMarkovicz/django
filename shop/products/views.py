from django.shortcuts import render
import logging
from django.http import HttpResponse
from django.conf import settings
from products.models import Product

logger = logging.getLogger(__name__)

# Create your views here.


def index(request):
    return HttpResponse(f"This is the Main Page.")


def products_view(request):
    if request.GET.get("product"):
        product = Product.objects.filter(title__contains=f"{request.GET.get('product')}").first()
        return HttpResponse(f"""Title: {product.title},
        Price: {product.price},
        Description: {product.description}""")
    product_list = Product.objects.all()
    return HttpResponse(f"""All products:
{[product.title for product in product_list]}""")
