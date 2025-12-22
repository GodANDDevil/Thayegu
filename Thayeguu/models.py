from django.db import models

# Create your models here.
class User(models.Model):
    user_phonenumber = models.CharField(max_length=10)
    user_name = models.CharField(max_length=100)
    user_gmail = models.EmailField(unique=True)
    user_password = models.CharField(max_length=100)

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.FileField(null=True,blank=True,upload_to='product_images/')
    product_payment_method = models.FileField(null=True,blank=True,upload_to='payment_methods/')

class Ads(models.Model):
    ads_name = models.CharField(max_length=100)
    ads_description = models.TextField()
    ads_price = models.DecimalField(max_digits=10, decimal_places=2)
    ads_image = models.FileField(null=True,blank=True,upload_to='ads_images/')
    ads_payment_method = models.FileField(null=True,blank=True,upload_to='payment_methods/')

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.user_name} - {self.product.product_name} ({self.quantity})"
