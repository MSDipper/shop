from django.shortcuts import render


from shop.models import Product

def shop(request):
    product = Product.objects.all()[:6]
    context = {
        'product_list':product,
    }
    return render(request, 'shop/shop_list.html', context)