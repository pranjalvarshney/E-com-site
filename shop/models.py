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

class Banner(models.Model):
    banner_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=50,default='')
    description = models.CharField(max_length=200,default='')
    bgimage = models.ImageField(upload_to="shop/images/banner/bg",default='')
    image = models.ImageField(upload_to="shop/images/banner/img",default='')

    def __str__(self):
        return self.title

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=50)
    update_desc = models.CharField(max_length=50)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self): 
        return self.order_id + " Status:  " + self.update_desc