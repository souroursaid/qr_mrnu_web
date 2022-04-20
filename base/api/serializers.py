from dataclasses import field
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from base.models import *


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class TableSerializer(ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class CallWaiterSerializer(ModelSerializer):
    class Meta:
        model = Call_waiter
        fields = '__all__'


class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class OrderItemSerializer(ModelSerializer):

    def restore_object(self, attrs, instance=None):
        assert instance is None, 'Cannot update users with UserFromEmailSerializer'

        (user_object, created) = Customer().objects.get_or_create(
            email=attrs.get('email')
        )

        # You can extend here to work on `user_object` as required - update etc.

        return user_object

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
