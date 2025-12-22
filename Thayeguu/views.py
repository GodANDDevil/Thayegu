from django.shortcuts import render,redirect, get_object_or_404
from .models import User,Product,Ads,Cart

def FristPage(request):
    ads_data = Ads.objects.all()

    return render(request,'Frist.html',{'ads':ads_data})

def RegisterPage(request):
    from django.db import connection
    print("Using DB:", connection.settings_dict['NAME'])

    if request.method == "POST":
        phonenumber = request.POST.get('phonenumber')
        name = request.POST.get('name')
        gmail = request.POST.get('gmail')
        password = request.POST.get('password')

        data = User(
            user_phonenumber=phonenumber,
            user_name=name,
            user_gmail=gmail,
            user_password=password
        )
        data.save()
        return render(request,'LoginPage.html')

    return render(request,'Register.html')

def LoginPage(request):
    if request.method == "POST":
        name = request.POST.get('name')
        gmail = request.POST.get('gmail')
        password = request.POST.get('password')
        try:
            user = User.objects.get(user_gmail=gmail)
            if user.user_password == password:
                request.session['user_name']=user.user_name
                return redirect('Home')
            else:
                return render(request, 'LoginPage.html', {'error_message': 'Invalid password'})
        except User.DoesNotExist:
            return render(request, 'LoginPage.html', {'error_message': 'User does not exist'})
        

    return render(request,'LoginPage.html')

def HomePage(request):
    ads_data = Ads.objects.all()
    product_data = Product.objects.all()
    print("Ads:", Ads.objects.count())
    print("Products:", Product.objects.count())
    print("Template loaded")
    return render(request,'HomePage.html',{'ads':ads_data,'products':product_data})

def AdsPage(request, id):
    ads_data = get_object_or_404(Ads, id=id)
    
    return render(request,'Ads.html',{'ads':ads_data})

def Products(request, id):
    product_data = get_object_or_404(Product, id=id)

    return render(request,'Product.html',{'product':product_data})

def PaymentPage(request):
    return render(request,'PaymentPage.html')

def cart_page(request):
    if request.session.get('user_name'):
        user = User.objects.get(user_name=request.session['user_name'])
        cart_items = Cart.objects.filter(user=user)

    else:
        cart_items = []
    total = sum(item.product.product_price for item in cart_items)

    return render(request,"Cart.html",{'cart_items':cart_items, 'total':total})

def AddToCart(request,product_id):
    product = Product.objects.get(id=product_id)
    user = User.objects.get(user_name=request.session['user_name'])
    cart_item, created = Cart.objects.get_or_create(user=user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect("Cart")

def clear_cart(request):
    if request.session.get('user_name'):
        user = User.objects.get(user_name=request.session['user_name'])
        Cart.objects.filter(user=user).delete()
    return redirect('Cart')

def SellPage(request):
    if request.method == "POST":
        product_name = request.POST.get('productname')
        product_description = request.POST.get('productdescription')
        product_price = request.POST.get('price')
        product_image = request.FILES.get('productimage')

        data = Product(
            product_name=product_name,
            product_description=product_description,
            product_price=product_price,
            product_image=product_image
        )
        data.save()
        return redirect('Sell')

    return render(request,'SellPage.html')

def ContactPage(request):
    return render(request,'ContactPage.html')

def AboutPage(request):
    return render(request,'AboutPage.html')