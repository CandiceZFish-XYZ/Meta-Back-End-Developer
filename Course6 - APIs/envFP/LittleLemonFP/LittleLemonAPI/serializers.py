from django.forms import ValidationError
from rest_framework import serializers
from .models import Category, MenuItem, Cart

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
    # class Meta:
    #     model = Cart
    #     fields = '__all__'
    menuitem = MenuItemSerializer
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
