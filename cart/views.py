from django.shortcuts import render, get_object_or_404
from shop.models import Product
from django.views.decorators.http import require_POST
from .cart import Cart
from django.http import JsonResponse


# Create your views here.
@require_POST
def add_to_cart(request, product_id):
    try:
        product = get_object_or_404(Product, id=product_id)
        cart = Cart(request)
        cart.add(product)
        context = {
            'item_count': len(cart),
            'total_price': cart.get_total_price()
        }
        return JsonResponse(context)
    except:
        return JsonResponse('error')
