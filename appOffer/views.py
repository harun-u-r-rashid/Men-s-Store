
from django.shortcuts import render, get_object_or_404
from appStore.models import Product, Review
from appCategory.models import Category

def discount_store(request, category_slug=None):
    categories = Category.objects.all()
    # reviews = Review.objects.filter(is)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        discount_products = Product.objects.filter(category=category, is_discount=True)
    else:
        discount_products = Product.objects.filter(is_discount=True)

    for product in discount_products:
        product.price = product.discount_price()
   
    return render(request, 'discount_store.html', {
        'categories': categories,
        'discount_products': discount_products,
    })






































# from django.shortcuts import render, get_object_or_404, redirect
# from .models import DiscountProduct, DiscountCategory
# from django.core.paginator import Paginator

# def discount_store(request, disCategorySlug = None):
#         if disCategorySlug:
#                 category = get_object_or_404(DiscountCategory, slug = disCategorySlug)
#                 dis_products = DiscountProduct.objects.filter(is_available = True, category = category)
#                 page = request.GET.get('page')
#                 paginator = Paginator(dis_products, 8)
#                 pagedDisProducts = paginator.get_page(page)
#         else:
#                 dis_products = DiscountProduct.objects.filter(is_available = True)
#                 paginator = Paginator(dis_products, 8)
#                 page = request.GET.get('page')
#                 pagedDisProducts = paginator.get_page(page)

#                 for pageDisProduct in pagedDisProducts:
#                        print(pageDisProduct)

#                 print(pagedDisProducts.has_next(), pagedDisProducts.has_previous(), pagedDisProducts.previous_page_number, pagedDisProducts.next_page_number)

#         dis_categories = DiscountCategory.objects.all()
#         context = {'dis_products':pagedDisProducts, 'dis_categories': dis_categories}
#         return render(request, 'discount_store.html', context)


# def discount_product_detail(request, disCategorySlug, disProductSlug):
#     singleDisProduct = get_object_or_404(DiscountProduct, category__slug=disCategorySlug, slug=disProductSlug)

#     return render(request, 'discount_product_details.html', {'product': singleDisProduct})

