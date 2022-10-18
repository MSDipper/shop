from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from shop.models import Product
from cart.forms import CartAddProductForm

class ShopListView(ListView):
    model = Product
    paginate_by = 3
    template_name = 'shop/product_list.html'
    
    def get_queryset(self):
        return Product.objects.filter(published=True)
    
    
    
def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                published=True
                                )
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form':cart_product_form,
    }
    return render(request,'shop/product_detail.html', context)