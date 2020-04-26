from django.db import models

# Create your models here.
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