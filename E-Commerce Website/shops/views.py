from django.shortcuts import render, redirect, HttpResponse
from shops.forms import CustomUserForm
from . models import *
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
import json

def home(request):
    products = Product.objects.filter(trending=1)
    return render(request, 'shops/index.html', {"products": products})
def cart_page(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        return render(request, 'shops/cart.html', {"cart": cart})
    else:
        return redirect("/")
    
def add_to_cart(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.load(request)
            product_qty = data['product_qty']
            product_id = data['pid']
            #print(request.user.id)
            product_status = Product.objects.get(id=product_id)
            if product_status:
                if Cart.objects.filter(user=request.user.id, product_id=product_id):
                    return JsonResponse({'status': 'Product already exists'}, status=200)
                else:
                    if product_status.quantity >= product_qty:
                        Cart.objects.create(user=request.user, product_id=product_id, product_qty=product_qty)
                        return JsonResponse({'status': 'Product successfully added to the cart'}, status=200)
                    else:
                        return JsonResponse({'status': 'Stock not available'}, status=200)
            
        else:
            return JsonResponse({'status': 'Login to add cart'}, status=200)
    else:
        return JsonResponse({'status': 'Invalid Access'}, status=200)

def remove_cart(request, cid):
    cartitem = Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect("/cart")

def favviewpage(request):
    if request.user.is_authenticated:
        fav = Favourite.objects.filter(user=request.user)
        return render(request, 'shops/fav.html', {"fav": fav})
    else:
        return redirect("/")

def remove_fav(request, fid):
    item = Favourite.objects.get(id=fid)
    item.delete()
    return redirect("/favviewpage")
    
def fav_page(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.load(request)
            product_id = data['pid']
            product_status = Product.objects.get(id=product_id)
            if product_status:
                if Favourite.objects.filter(user=request.user.id, product_id=product_id):
                    return JsonResponse({'status': 'Product already in favourite'}, status=200)
                else:                    
                    Favourite.objects.create(user=request.user, product_id=product_id)  
                    return JsonResponse({'status': 'Product added to favourite'}, status=200)      
        else:
            return JsonResponse({'status': 'Login to add favourite'}, status=200)
    else:
        return JsonResponse({'status': 'Invalid Access'}, status=200)
 
def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request, username=name, password=pwd)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password")
                return redirect('/login')
  
    return render(request, "shops/login.html")

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logout successful")
    return redirect("/")
  
def register(request):
    form = CustomUserForm()
    if (request.method == 'POST'):
        form = CustomUserForm(request.POST)
        if (form.is_valid()):
            form.save()
            messages.success(request, "Registration successful")
            return redirect('/login')
    return render(request, 'shops/registers.html', {'form': form})

def collections(request):
    category = Category.objects.filter(status=0)
    return render(request, 'shops/collections.html', {'category': category})

def collectionsview(request, name):
    if (Category.objects.filter(status=0)):
        products = Product.objects.filter(category__name=name)
        return render(request, 'shops/products/index.html', {'products': products, "category_name": name})
    else:
        messages.warning(request, "No such category found")
        return redirect('collections')
        
def product_details(request, cname, pname):
    if (Category.objects.filter(name=cname, status=0)):
        if (Product.objects.filter(name=pname, status=0)):
            products = Product.objects.filter(name=pname, status=0).first()
            return render(request, "shops/products/product_details.html", {"products": products})   
        else:
            messages.error(request, "No such product found")
            return redirect('collections')
    else:
        messages.error(request, "No such category found")
        return redirect('collectons')

    