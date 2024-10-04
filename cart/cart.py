from shop.models import Product


class Cart:
    def __init__(self, request):
        self.request = request.session
        cart = self.request.get['cart']

        if not cart:
            cart = self.request['cart'] = {}
        self.cart = cart
