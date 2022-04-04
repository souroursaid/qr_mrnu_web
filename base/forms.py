from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import *


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required': '',
            'name': 'username',
            'id': 'username',
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'type your username',
            'maxlength': '16',
            'minlength': '6',
        })
        self.fields["email"].widget.attrs.update({
            'required': '',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'class': 'form-control',
            'placeholder': 'type your email',
        })

        self.fields["password1"].widget.attrs.update({
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'class': 'form-control',
            'placeholder': 'type your password',
            'maxlength': '22',
            'minlength': '8',
        })
        self.fields["password2"].widget.attrs.update({
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'class': 'form-control',
            'placeholder': 'type your password',
            'maxlength': '22',
            'minlength': '8',
        })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({
            'required': '',
            'name': 'name',
            'class': 'form-control',
        })

    class Meta:
        model = Category
        fields = '__all__'


class TableForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["table_Number"].widget.attrs.update({
            'required': '',
            'name': 'table_Number',
            'id': 'table_Number',
            'type': 'number',
            'class': 'form-control',
            'placeholder': 'enter a number',

        })
        self.fields["size"].widget.attrs.update({
            'required': '',
            'name': 'size',
            'id': 'size',
            'type': 'number',
            'class': 'form-control',
            'placeholder': 'enter a size',
        })

    class Meta:
        model = Table
        fields = '__all__'


class MenuForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].widget.attrs.update({
            'required': '',
            'name': 'category',
            'class': 'form-control',
        })
        self.fields["name"].widget.attrs.update({
            'required': '',
            'name': 'name',
            'type': 'text',
            'class': 'form-control',
        })

        self.fields["price"].widget.attrs.update({
            'required': '',
            'name': 'price',
            'type': 'number',
            'class': 'form-control',

        })
        self.fields["image"].widget.attrs.update({
            'required': '',
            'name': 'image',

            'type': 'image',
            'class': 'form-control',

        })
        self.fields["description"].widget.attrs.update({
            'name': 'description',
            'type': 'text',
            'class': 'form-control',
        })

    class Meta:
        model = Menu
        fields = '__all__'


class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["place_order"].widget.attrs.update({
            'required': '',
            'name': 'place_order',
            'class': 'form-control',
        })
        self.fields["table"].widget.attrs.update({
            'required': '',
            'name': 'table',
            'type': 'text',
            'class': 'form-control',
        })
        self.fields["customer"].widget.attrs.update({
            'name': 'customer',
            'type': 'text',
            'class': 'form-control',
        })

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["menu"].widget.attrs.update({
            'required': '',
            'name': 'menu',
            'class': 'form-control',
        })
        self.fields["order"].widget.attrs.update({
            'required': '',
            'name': 'order',
            'class': 'form-control',
        })
        self.fields["quantity"].widget.attrs.update({
            'name': 'quantity',
            'type': 'text',
            'class': 'form-control',
        })

    class Meta:
        model = OrderItem
        fields = '__all__'


class ReservationForm(ModelForm):

    class Meta:
        model = Reservation
        fields = '__all__'


class RestaurantForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["restaurant_name"].widget.attrs.update({
            'required': '',
            'name': 'restaurant_name',
            'class': 'form-control',
        })
        self.fields["email"].widget.attrs.update({
            'required': '',
            'name': 'email',
            'type': 'email',
            'class': 'form-control',
        })
        self.fields["phone"].widget.attrs.update({
            'name': 'phone',
            'type': 'text',
            'class': 'form-control',
        })
        self.fields["address"].widget.attrs.update({
            'name': 'address',
            'type': 'text',
            'class': 'form-control',
        })
        self.fields["city"].widget.attrs.update({
            'name': 'city',
            'type': 'text',
            'class': 'form-control',
        })
        self.fields["zipcode"].widget.attrs.update({
            'name': 'zipcode',
            'type': 'text',
            'class': 'form-control',
        })

    class Meta:
        model = Restaurant
        fields = '__all__'

