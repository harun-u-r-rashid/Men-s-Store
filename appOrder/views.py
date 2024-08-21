from django.shortcuts import render, redirect
from appCart.models import CartItem
from .forms import OrderForm 
from .ssl import sslcommerz_payment_gateway
from .models import Payment, Order, OrderProduct
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from appStore.models import Product
from .forms import OrderForm 
from .ssl import sslcommerz_payment_gateway
from appAuth import models
from .models import Payment, Order, OrderProduct
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from appStore.models import Product
from django.shortcuts import redirect
from django.contrib import messages


#@method_decorator(csrf_exempt, name='dispatch') #An error is showing while using this

@csrf_exempt
def successView(request):
    data = request.POST
    user_id = int(data['value_b'])
    user = models.User.objects.get(pk=user_id)
    payment = Payment(
        user=user,
        payment_id=data['tran_id'],
        payment_method=data['card_issuer'],
        amount_paid=int(data['store_amount'][0]),
        status=data['status'],
    )

    payment.save()

    order = Order.objects.get(user=user, is_ordered=False, order_number=data['value_a'])
    order.payment = payment
    order.is_ordered = True
    order.save()

    cart_items = CartItem.objects.filter(user=user)

    for item in cart_items:
        orderProduct = OrderProduct()
        product = Product.objects.get(id=item.product.id)
        orderProduct.order = order
        orderProduct.payment = payment
        orderProduct.user = user
        orderProduct.product = product
        orderProduct.quantity = item.quantity
        orderProduct.ordered = True
        orderProduct.save()
        product.stock -= item.quantity
        product.save()

    CartItem.objects.filter(user=user).delete()
    return redirect('cart')


@csrf_exempt
def failView(request):
       return render(request, 'appOrder/failedOrder.html')





# For complete order view page
def orderComplete(request):
        return render(request, 'appOrder/orderComplete.html')



def checkout(request):
        cart_items = None
        tax = 0
        total = 0
        grand_total = 0


        cart_items = CartItem.objects.filter(user = request.user)

        if cart_items.count() < 1:
                messages.error(request,"Add item to the cart.")
                return redirect('store')
        

        for item in cart_items:
                # print('item',item)
                # print('item',item.product.price)
                if(item.product.is_discount):
                              item.product.price=item.product.discount_price()
                # print('item',item)
                print('item',item.product.price)
                total += item.product.price * item.quantity

        tax = (2*total)/100

        grand_total += total + tax

        if request.method == 'POST':
                form = OrderForm(request.POST)
                if form.is_valid():
                        form.instance.user = request.user
                        form.instance.order_total = grand_total
                        form.instance.tax = tax
                        form.instance.ip = request.META.get('REMOTE_ADDR')
                        form.instance.payment = 2
                        saved_instance = form.save()
                        form.instance.order_number = saved_instance.id
                        form.save()
                        return redirect(sslcommerz_payment_gateway(request, saved_instance.id, str(request.user.id), grand_total))
        return render(request, 'appOrder/placeOrder.html', {'cart_items':cart_items, 'tax':tax, 'total':total, 'grand_total':grand_total})




def orderHistory(request):
     orders = Order.objects.filter(user=request.user)
     return render(request, 'appOrder/orderHistory.html', {'orders': orders})



def orderDetails(request, orderId):
       order = Order.objects.get(id = orderId)
       orderProducts = OrderProduct.objects.filter(order=order)
       total = 0
       for orderProduct in orderProducts:
              if(orderProduct.product.is_discount): #This may be give wrong have to check after render
                              orderProduct.product.price=orderProduct.product.discount_price()
        #       print('order',orderProduct)
              total += orderProduct.product.price*orderProduct.quantity
       tax = (total/100)*2

       grand_total = total + tax
       return render(request, 'appOrder/orderDetails.html', {'order':order, 'orderProducts':orderProducts, 'total':total, 'tax':tax, 'grand': grand_total})

       


def payment(request):
       payment = Payment.objects.filter(user = request.user)
       return render(request, 'appOrder/payment.html', {'payment':payment})
 

    
