from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(Table)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Call_waiter)
admin.site.register(Reservation)
admin.site.register(Feedback)
admin.site.register(Restaurant)
admin.site.register(QrCode)


