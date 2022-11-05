from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from shop.models import Product, Brand, Color, Comment
from cart.forms import CartAddProductForm
from django.db.models import Count, Q
from shop.forms import CommentForm, ReviewForm
from django.views.generic.base import View


class BrandColor:
    """ Фильтрация по брендамcart_product_form и цвету """
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
        return Product.objects.filter(published=True)
    
    
class CreateComment(View):
    """ Отзывы """
    def post(self, request, pk):
        form = CommentForm(request.POST)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.product = product
            form.save()
        return redirect(product.get_absolute_url())  


class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.product = product
            form.save()
        return redirect(product.get_absolute_url())


class ProductDetailView(DetailView):
    """ Полное описание продукта """
    model = Product
    template_name = 'shop/product_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm() # Форма выбора кол-ва и добавление в карзину
        context['form'] = CommentForm()
        context['form_review'] = ReviewForm()
        return context
    
    
# def product_detail(request, id, slug):
    #     """ Полное описание продукта """
    #     product = get_object_or_404(Product,
    #                                 id=id,
    #                                 slug=slug,
    #                                 published=True
    #                                 )
    #     return product
    
    # cart_product_form = CartAddProductForm() 
    
    # context = {
    #     'product': product,
    #     'cart_product_form':cart_product_form,
    # }
    # return render(request,'shop/product_detail.html', context)


class FilterProduct(BrandColor, ListView):
    ''' Фильтр фильмов '''
    def get_queryset(self):
        queryset = Product.objects.filter(
            Q(brand__in=self.request.GET.getlist('brand')) | Q(color__in=self.request.GET.getlist('color')))
        return queryset


