from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from appCart.models import Cart, CartItem
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator 
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import CustomSetPasswordForm, UpdateProfileForm
from appOrder.models import Order
from appStore.models import Product, Category
from django.core.paginator import Paginator


def get_create_session(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key


def home(request):
        return render(request, 'appAuth/home.html')



def account(request):
        return render(request, 'appAuth/account.html')




def register(request):
        form = RegistrationForm()
        if request.method == "POST":
                form = RegistrationForm(request.POST)

                if form.is_valid():
                        user = form.save(commit = False)
                        user.is_active = False
                        user.backend = 'django.contrib.auth.backends.ModelBackend'
                        user.save()

                        current_site = get_current_site(request)
                        mail_subject = "Please active your account!"
                        message = render_to_string('appAuth/email_verification.html', {
                              'user' : user,
                              'domain': current_site,
                              'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                              'token' : default_token_generator.make_token(user),
                        })

                        to_email = user.email
                        send_email = EmailMessage(mail_subject, message, to=[to_email])
                        send_email.send()
                        return HttpResponse('Please confirm your email to complete the registration')

        else:
              form = RegistrationForm()
                
        return render(request, 'appAuth/register.html', {'form':form})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk = uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
         user.is_active = True
         user.save()

         messages.success(request, 'Congratulations, your account has been activated.')
         return redirect('login')
    else:
         messages.error(request, 'Invalid activation link')
    
    return redirect('register')

         
def userLogin(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = user_name, password = password)

        if user is not None:
             
          session_key = get_create_session(request)
          cart = Cart.objects.filter(cart_id = session_key).exists()
          print("cart", cart)
          if cart:
               cart = Cart.objects.get(cart_id = session_key)
               print("s cart", cart)
               is_cart_item_exists = CartItem.objects.filter(cart = cart).exists()
               if is_cart_item_exists:
                    cart_item = CartItem.objects.filter(cart = cart)
                    for item in cart_item:
                         item.user = user
                         item.save()
          login(request, user)
          return redirect('home')
    return render(request, 'appAuth/login.html')


def userLogout(request):
        logout(request)
        return redirect('login')



def resetPassword(request):
     if request.method == "POST":
          email = request.POST['email']

          if User.objects.filter(email = email).exists():
               user = User.objects.get(email__exact = email)


               current_site = get_current_site(request)
               email_subject = 'Reset your password'
               messages = render_to_string('appAuth/reset_password_email.html', {
                    'user':user,
                    'domain': current_site,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
               })

               to_email = email
               send_email = EmailMessage(email_subject, messages, to=[to_email])
               send_email.send()
               return redirect('login')
          else:
               return redirect('forget_password')
     return render(request, 'appAuth/reset_password.html')



def activate_reset_password(request, uidb64, token):
     try:
          uid = urlsafe_base64_decode(uidb64).decode()
          user = User._default_manager.get(pk = uid)

     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
          user = None


     if user is not None and default_token_generator.check_token(user, token):
          if request.method == 'POST':
               form = CustomSetPasswordForm(user, request.POST)
               if form.is_valid():
                    user = form.save()
                    update_session_auth_hash(request, user)
                    return redirect('login')
          else:
               form = CustomSetPasswordForm(user)
          return render(request, 'appAuth/reset_form.html', {'form':form})
     
     else:
          messages.error(request, 'Invalid Link')

     return redirect('register')



def updateProfile(request):
     user = request.user
     form = UpdateProfileForm()
     if request.method == 'POST':
          form = UpdateProfileForm(request.POST, instance = user)
          if form.is_valid():
               form.save()
               return redirect('account')
     return render(request, 'appAuth/updateProfile.html', {'form':form})





