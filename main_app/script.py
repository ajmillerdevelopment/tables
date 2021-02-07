from .models import *

def subtot(order_id):
    o = Order.objects.get(id=order_id)
    for item in o.items.all:
        print(item)

subtot(31)