from django.shortcuts import render
import logging
from django.http import HttpResponse
from django.conf import settings
from products.models import Product
from django.db.models import Sum, Count, Q

logger = logging.getLogger(__name__)


# Create your views here.


def index(request):
    return HttpResponse(f"This is the Main Page.")


def products_view(request):
    product_list = Product.objects.all()
    if request.GET.get("title") is not None:
        product_list = product_list.filter(title__icontains=request.GET.get("title"))
    if request.GET.get("purchases_count") is not None:
        product_list = product_list.filter(purchases__count=request.GET.get("purchases_count"))
    if request.GET.get("price") is not None:
        product_list = product_list.filter(product__price=request.GET.get("price"))
    # if request.GET.get("purchases_revenue") is not None:  # Неправильно
    #     price_list = [product.price for product in product_list]
    #     count_list = [list(Product.objects.aggregate(count=Sum("purchases__count", filter=Q(price=price))).values()) for price in price_list]
    #     count_list = sum(count_list, [])
    #     purchases_revenue_list = [count_list[i] * price_list[i] for i in range(len(price_list))]
    #     print(purchases_revenue_list)
    return HttpResponse(f"{'<br>'.join([str(product) for product in product_list])}")
