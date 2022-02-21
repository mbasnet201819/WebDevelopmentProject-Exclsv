from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    image = models.FileField(upload_to='product_images')
    productname = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)
    finalprice = models.CharField(max_length=100)
    previousprice = models.CharField(max_length=100)


    class Meta:
        db_table = "product"
# Create your models here.
class Order(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    fullname = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)


    class Meta:
        db_table = "order"
