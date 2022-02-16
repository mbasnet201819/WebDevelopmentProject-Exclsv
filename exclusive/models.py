from django.db import models

from django.db import models


# Create your models here.
class Customer(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)

    class Meta:
        db_table = "Customer"
