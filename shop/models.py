from django.db import models

# Create your models here.
class Contact(models.Model):
    query_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default='')
    email = models.EmailField(max_length=50,default='')
    phone = models.CharField(max_length=10,default='')
    query = models.CharField(max_length=2000,default='')

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    sub_category = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images",default="")
    description = models.CharField(max_length=500)
    published_date = models.DateField()

    def __str__(self):
        return self.product_name



