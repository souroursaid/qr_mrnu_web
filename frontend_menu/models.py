from django.db import models
from base.models import *

# Create your models here.

class Checkout(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.address