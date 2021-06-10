from .models import Category
from .utils import Basket, cartData


def categories(request):
    return {'categories': Category.objects.all()}


def basket(request):
    return {'basket': Basket(request)}

def cartItems(request):
    data = cartData(request)
    cartItems = data['cartItems']
    return {'cart_items': cartItems}
