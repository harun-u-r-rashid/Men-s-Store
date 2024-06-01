from django.shortcuts import render, redirect
from appStore.models import Product
from .models import Cart, CartItem





def get_create_session(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key





def cart(request):
        cart_items = None
        tax = 0
        total = 0
        grand_total = 0
        session_id = get_create_session(request)
        if request.user.is_authenticated:
                cart_items = CartItem.objects.filter(user = request.user)
                combined_quantities = {}
                for cart_item in cart_items:
                        product_id = cart_item.product_id
                        if product_id in combined_quantities:
                                combined_quantities[product_id] += cart_item.quantity
                                # Deactivate the current cart item
                                cart_item.is_active = False
                                cart_item.save()
                        else:
                                combined_quantities[product_id] = cart_item.quantity
                for item in cart_items:
                        total += item.product.price * item.quantity
        else:
                cartid = Cart.objects.get(cart_id = session_id) # model ke ber kore anlam
                cart_id = Cart.objects.filter(cart_id = session_id).exists() # ei session id wala kono cart amader database e ache kina
                print(cart_id)
                if cart_id:
                        cart_items = CartItem.objects.filter(cart = cartid)
                        for item in cart_items:
                                total += item.product.price * item.quantity
        
        tax = (2*total)/100
        grand_total = total + tax
                
        return render(request, 'appCart/cart.html' ,{'cart_items' : cart_items, 'tax' : tax,'total' : total, 'grand_total' : grand_total})






# def addToCart(request, product_id):
#     product = Product.objects.get(id=product_id)
#     session_id = get_create_session(request) 

#     if request.user.is_authenticated:
#         cart_item = CartItem.objects.filter(product=product, user = request.user).exists()
#         if cart_item:
#             item = CartItem.objects.get(product=product)
#             item.quantity += 1
#             item.save()
#         else :
#             cartid = Cart.objects.get(cart_id = session_id)
#             item = CartItem.objects.create(
#                 cart = cartid,
#                 product = product,
#                 quantity = 1,
#                 user = request.user
#             )
#             item.save()
#     else:
#           return redirect('login')
#         # print(session_id)
#         # cart_id = Cart.objects.filter(cart_id = session_id).exists()
#         # if cart_id:
#         #     cartid = Cart.objects.get(cart_id = session_id)
#         #     cart_item = CartItem.objects.filter(product=product, cart = cartid).exists()
#         #     if cart_item:
#         #         item = CartItem.objects.get(product=product, cart= cartid)
#         #         item.quantity += 1
#         #         item.save()
#         #     else :
#         #         cartid = Cart.objects.get(cart_id = session_id)
#         #         print("adfasdf ", cartid, session_id)
#         #         item = CartItem.objects.create(
#         #             cart = cartid,
#         #             product = product,
#         #             quantity = 1
#         #         )
#         #         item.save()
#         # else:
            
#         #     cart = Cart.objects.create(
#         #     cart_id = session_id
#         #     )
#         #     cart.save()
#         #     cartid = Cart.objects.get(cart_id = session_id)
#         #     item = CartItem.objects.create(
#         #           cart = cartid, 
#         #           product = product,
#         #           quantity = 1
#         #     )
#         #     item.save()
    
#     return redirect('cart')


def addToCart(request, product_id):
    product = Product.objects.get(id=product_id)
    session_id = get_create_session(request) 

    if request.user.is_authenticated:
        cart_id = Cart.objects.filter(cart_id = session_id)
        if cart_id:
            cart_item = CartItem.objects.filter(product=product, user = request.user).exists()
            if cart_item:
                item = CartItem.objects.get(product=product, user = request.user)
                item.quantity += 1
                item.save()
            else :
                cartid = Cart.objects.get(cart_id = session_id)
                cart_item = CartItem.objects.create(
                    cart = cartid,
                    product = product,
                    quantity = 1,
                    user = request.user
                )
                cart_item.save()
        else:
            cart = Cart.objects.create(
                cart_id = session_id
              )
            cart.save()

            cart_item = CartItem.objects.filter(product = product, user = request.user).exists()
            if cart_item:
                item = CartItem.objects.get(product=product, user = request.user)
                item.quantity+=1
                item.save()
            else:
                  cartid = Cart.objects.get(cart_id=session_id)
                  cart_item = CartItem.objects.create(
                        user = request.user,
                        product = product,
                        quantity = 1,
                        cart = cartid
                  )
                  cart_item.save()
            
              
    else:
        # User that are not authenticated can't add item to the cart
        return redirect('login')
        # Non authenticated user
        # print(session_id)
        # cart_id = Cart.objects.filter(cart_id = session_id).exists()
        # if cart_id:
        #     cartid = Cart.objects.get(cart_id = session_id)
        #     cart_item = CartItem.objects.filter(product=product, cartid = session_id).exists()
        #     if cart_item:
        #         item = CartItem.objects.get(user = None, product=product, cart_id  = session_id)
        #         item.quantity += 1
        #         item.save()
        #     else :
        #         cartid = Cart.objects.get(cart_id = session_id)
        #         print("adfasdf ", cartid, session_id)
        #         item = CartItem.objects.create(
        #             cart = cartid,
        #             product = product,
        #             quantity = 1
        #         )
        #         item.save()
        # else:
            
        #     cart = Cart.objects.create(
        #     cart_id = session_id
        #     )
        #     cart.save()
        #     cartid = Cart.objects.get(cart_id = session_id)
        #     item = CartItem.objects.create(
        #           cart = cartid, 
        #           product = product,
        #           quantity = 1
        #     )
        #     item.save()
    
    return redirect('cart')





def removeCartItem(request, product_id):
      session_id = request.session.session_key
      product = Product.objects.get(id = product_id)
      
      if request.user.is_authenticated:    
        cart_item = CartItem.objects.get(user = request.user, product = product)
        if cart_item.quantity>1:
                cart_item.quantity-=1
                cart_item.save()
        else:
                cart_item.delete()
       
      return redirect('cart')


