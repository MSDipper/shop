from django.shortcuts import render
from orders.models import OrderItemList
from orders.forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItemList.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'orders/checkout.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/checkout.html',
                  {'cart': cart, 'form': form})