from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    image = models.FileField(upload_to='product_images')
    productname = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)
    finalprice = models.CharField(max_length=100)
    previousprice = models.CharField(max_length=100)

    # quantity = models.CharField(max_length=200)

    class Meta:
        db_table = "product"
