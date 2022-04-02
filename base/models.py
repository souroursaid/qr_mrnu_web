from django.db import models
from django.contrib.auth.models import User
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File

# Create your models here.
import random

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.IntegerField( null=True)
    email = models.EmailField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['-date_updated', '-date_created']

    def __str__ (self):
        return self.name
        
class Category(models.Model):
    name = models.CharField(max_length=200, null=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['-date_updated', '-date_created']

    def __str__(self):
        return self.name

class Menu(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['-date_updated', '-date_created']

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
        
    def __str__(self):
        return self.name

class Table(models.Model):
    table_Number = models.IntegerField(null=True)
    size = models.IntegerField(null=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['-date_updated', '-date_created']

    def __str__(self):
        return "Table - %s " % (self.table_Number)

class Order(models.Model):
    CLASSIFY = (
        ('Restaurant', 'Restaurant'),
        ('Delivery', 'Delivery'),

    )
    place_order = models.CharField(max_length=100, null=True, choices=CLASSIFY, blank=True)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_delivery = models.DateTimeField(auto_now=True, null=True)
    
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['-date_updated', '-date_created']

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    def __str__ (self):
        return "Order  %s " % (self.id)

class OrderItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)


    class Meta:
        ordering = ['-date_updated', '-date_created']

    @property
    def get_total(self):
        total = self.menu.price * self.quantity
        return total

    def __str__ (self):
        return "Order  %s " % (self.order.id)

class Call_waiter(models.Model):
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['-date_updated', '-date_created']
    
    def __str__ (self):
        return "Call  %s " % (self.id)

class Reservation(models.Model):
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, blank=True)
    number_people = models.IntegerField(null=True, blank=True)
    note = models.CharField(max_length=100, null=True)
    date_visit = models.DateTimeField(null=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['-date_updated', '-date_created']


class Feedback(models.Model):
    CLASSIFY = (
        ('Poor', 'Poor'),
        ('Good', 'Good'),
        ('Excellent', 'Excellent'),
    )
    ambiance = models.CharField(max_length=100, null=True, choices=CLASSIFY, blank=True)
    food = models.CharField(max_length=100, null=True, choices=CLASSIFY, blank=True)
    service = models.CharField(max_length=100, null=True, choices=CLASSIFY, blank=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, blank=True)
    suggestions = models.CharField(max_length=200, null=True, blank=True)

    date_updated = models.DateTimeField(auto_now=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-date_updated', '-date_created']

    def __str__(self):
        return "Feedback  %s " % (self.id)

class Contact_detail(models.Model):
    restaurant_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)

    date_updated = models.DateTimeField(auto_now=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-date_updated', '-date_created']

    def __str__(self):
        return self.restaurant_name

class QrCode(models.Model):
   url=models.URLField()
   image=models.ImageField(upload_to='qrcode',blank=True)

   def save(self,*args,**kwargs):
      qrcode_img=qrcode.make(self.url)
      canvas=Image.new("RGB", (400,400),"white")
      draw=ImageDraw.Draw(canvas)
      canvas.paste(qrcode_img)
      buffer=BytesIO()
      canvas.save(buffer,"png")
      self.image.save(f'image{random.randint(1, 1000)}.png',File(buffer),save=False)
      canvas.close()
      super().save(*args,**kwargs)
