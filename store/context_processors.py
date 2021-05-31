from .models import Category
from .utils import Basket


def categories(request):
    return {'categories': Category.objects.all()}


def basket(request):
    return {'basket': Basket(request)}
