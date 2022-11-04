from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from shop.models import Product, Brand, Color
from cart.forms import CartAddProductForm
from django.db.models import Count
from django.db.models import Q

class BrandColor:
    """ Фильтрация по брендам и цвету """
    def get_brand(self):
        return Brand.objects.annotate(brand_count=Count('product')).all()
    
    def get_color(self):
        return Color.objects.annotate(color_count=Count('product')).all()


class ShopListView(BrandColor, ListView):
    """ Список продуктов """
    model = Product
    paginate_by = 3
    template_name = 'shop/product_list.html'
    
    def get_queryset(self):
        return Product.objects.filter(published=True).select_related('category')
    
    
    
def product_detail(request, id, slug):
    """ Полное описание продукта """
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                published=True
                                )
    cart_product_form = CartAddProductForm() # Форма выбора кол-ва и добавление в карзину
    context = {
        'product': product,
        'cart_product_form':cart_product_form,
    }
    return render(request,'shop/product_detail.html', context)


class FilterProduct(BrandColor, ListView):
    ''' Фильтр фильмов '''
    def get_queryset(self):
        queryset = Product.objects.filter(
            Q(brand__in=self.request.GET.getlist('brand')) | Q(color__in=self.request.GET.getlist('color')))
        return queryset