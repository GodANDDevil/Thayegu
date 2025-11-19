from Thayeguu import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePage,name='Home'),
    path('',views.HomePage,name='Contact'),
    path('',views.HomePage,name='About'),
    path('',views.HomePage,name='Login'),
    path('',views.HomePage,name='Sell'),
]