from django.db import models
from django.contrib.auth.models import User

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
