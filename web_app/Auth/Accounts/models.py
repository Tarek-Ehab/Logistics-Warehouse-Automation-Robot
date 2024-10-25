from django.db import models
from datetime import datetime

from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=255, unique=True)



# Create your models here.

class Classification(models.Model):
    title = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.title


class Supplier(models.Model):
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    phone = models.CharField(max_length=20 , unique=True)
    email = models.EmailField(unique=True)
    product_count = models.PositiveIntegerField(default=0)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Buyer(models.Model):
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    phone = models.CharField(max_length=20 , unique=True)
    email = models.EmailField(unique=True)
    order_count = models.PositiveIntegerField(default=0)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Season(models.Model):
    name = models.CharField(max_length=120, unique=True)
    def __str__(self):
        return self.name
    
class Zone(models.Model):
    name = models.CharField(max_length=120, unique=True,blank = True,null = True)
    def __str__(self):
        return self.name

# Define l Car Only M4 Hay3ml Drop l 7aga Delw2ti 
class CarDrop(models.Model):
    deliveryy_status = [
        ('Active','Active'), 
        ('In active','In active'),
        ('Disconnect','Disconnect')
    ]

    # id = models.AutoField(primary_key=True)
    Car_ID = models.CharField(max_length=120, unique=True,null = True,blank=True)
    drop_name = models.CharField(max_length=120, unique=True)
    delivery_status = models.CharField(max_length=50,choices=deliveryy_status,default='In active')



    def __str__(self):
        return self.drop_name


# Define l shelfs bas
class Shelf(models.Model):
    name = models.CharField(max_length=50,unique=True)
    capacity = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField()
    def __str__(self):
        return self.name




class Product(models.Model):
    status_product = [
        ('In stock','In stock'), 
        ('out of stock ','out of stock '),
    ]

    name = models.CharField(max_length=120, unique=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,null=True, blank=True)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE, null=True)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE,)
    describtion = models.CharField(max_length=120, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, null=True, blank=True)
    qr_code = models.CharField(max_length=120,unique=True, null=True, blank=True)
    status = models.CharField(max_length=50,choices=status_product,default='In stock')
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def save(self, *args, **kwargs):
        if not self.classification_id:
            self.classification = Classification.objects.first()
        if not self.shelf_id:
            self.shelf = Shelf.objects.first()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


    def __str__(self):
        return self.name

class Order(models.Model): 
    deliveryy_status = [
        ('pending','pending'), 
        ('arrived','arrived'),
    ]
    product = models.ForeignKey(Product,  on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    # season = models.ForeignKey(Season, on_delete=models.CASCADE,  default=Season.objects.first().id)
    drop_name = models.ForeignKey(CarDrop, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    delivery_status = models.CharField(max_length=50,choices=deliveryy_status,null=True,blank=True)
    class Meta:
        ordering = ['-order_date']
        
    def save(self, *args, **kwargs):
        if not self.product_id:
            self.product = Product.objects.first()
        if not self.buyer_id:
            self.buyer = Buyer.objects.first()
        if not self.drop_name_id:
            self.drop_name = CarDrop.objects.first()
        super().save(*args, **kwargs)

        
    def __str__(self):
        return '{} {} {}'.format(self.product, self.quantity,self.drop_name)
 