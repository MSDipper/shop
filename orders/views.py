from django.shortcuts import render
from orders.models import OrderItemList, Order
from orders.forms import OrderCreateForm
from cart.cart import Cart
from orders.service import send_mess
from orders.tasks import order_created
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'admin/orders/order/detail.html',
                  {'order': order})


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon: 
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()    # сохраняем связанный купон и применяемую скидку
            for item in cart:
                OrderItemList.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            # запуск асинхронной задачи
            # order_created.delay(order.id)
            return render(request, 'orders/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/checkout.html',
                  {'cart': cart, 'form': form})