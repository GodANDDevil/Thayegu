from Thayeguu import views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.FristPage,name='Frist'),
    path('Home/',views.HomePage,name='Home'),
    path('Contact/',views.ContactPage,name='Contact'),
    path('About/',views.AboutPage,name='About'),
    path('Login/',views.LoginPage,name='Login'),
    path('Register/',views.RegisterPage,name='Register'),
    path('SellPage/',views.SellPage,name='Sell'),
    path('SellProduct/<int:id>',views.AdsPage,name='Ads'),
    path('SellProducts/<int:id>',views.Products,name='Products'),
    path('Payment/',views.PaymentPage,name='Payment'),
    path('Cart/',views.cart_page,name='Cart'),
    path('AddToCart/<int:product_id>/',views.AddToCart,name='AddToCart'),
    path('ClearCart/',views.clear_cart,name='ClearCart'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
