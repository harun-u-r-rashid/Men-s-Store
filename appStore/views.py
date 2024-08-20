from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review
from appCategory.models import Category
from django.core.paginator import Paginator
from .forms import ProductReviewForm
from django.contrib import messages




def store(request, categorySlug = None):
        if categorySlug:
                category = get_object_or_404(Category, slug = categorySlug)
                products = Product.objects.filter(is_available = True, is_discount=False, is_new=False, category = category)
                page = request.GET.get('page')
                paginator = Paginator(products, 8)
                pagedProducts = paginator.get_page(page)
        else:
                products = Product.objects.filter(is_available=True, is_discount=False, is_new=False)
                for product in products:
                        product.price=product.discount_price()
                paginator = Paginator(products, 4)
                page = request.GET.get('page')
                pagedProducts = paginator.get_page(page)

                for pageProduct in pagedProducts:
                       print(pageProduct)

                print(pagedProducts.has_next(), pagedProducts.has_previous(), pagedProducts.previous_page_number, pagedProducts.next_page_number)
        
        
        categories = Category.objects.all()
        reviews = Review.objects.filter(product__is_available=True)
        context = {'products':pagedProducts, 'categories': categories, 'reviews':reviews}
        return render(request, 'appStore/store.html', context)




def product_detail(request, categorySlug, productSlug):
        singleProduct = Product.objects.get(category__slug=categorySlug, slug=productSlug)
        reviews = Review.objects.filter(product = singleProduct)
        regular_price = singleProduct.price
        discount_price=singleProduct.price-singleProduct.discount
        form = ProductReviewForm()
        if request.user.is_authenticated: 
                        if request.method == 'POST':
                                form = ProductReviewForm(request.POST)
                                if form.is_valid():
                                        form.instance.user = request.user
                                        form.instance.product = singleProduct
                                        review = form.save(commit=False)
                                        if Review.objects.filter(user = request.user, product = singleProduct).exists():
                                                messages.error(request, "You already added the review!")

                                        else:
                                                review.save()
                                        return redirect('home')
                        else:
                                form = ProductReviewForm()
        messages.error(request, "Sorry, you aren't an authorized user!")
        return render(request, 'appStore/productDetails.html', {'product' : singleProduct, 'regular_price':regular_price, 'discount_price':discount_price,  'form':form, 'reviews':reviews})








    


        
    
