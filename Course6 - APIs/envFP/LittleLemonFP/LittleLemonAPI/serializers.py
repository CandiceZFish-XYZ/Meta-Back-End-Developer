from django.forms import ValidationError
from rest_framework import serializers
from .models import Category, MenuItem, Cart, Order, OrderItem
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'featured', 'category', 'category_id']
        extra_kwargs = {
            'price': {'min_value': 2},
        }

class CartSerializer(serializers.ModelSerializer):
    menuitem = MenuItemSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = ['id', 'menuitem', 'quantity', 'unit_price', 'price']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def validate(self, data):
        user = self.context['request'].user
        menuitem = data['menuitem']
        if Cart.objects.filter(user=user, menuitem=menuitem).exists():
            raise ValidationError('A cart item with this menu item already exists for this user.')
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    menuitem = MenuItemSerializer(read_only=True)
    class Meta:
        model = OrderItem
        fields = '__all__'
