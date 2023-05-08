from uu import Error
from django.forms import model_to_dict
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User, Group

from .models import MenuItem, Cart, Order, OrderItem
from .serializers import MenuItemSerializer, CartSerializer, UserSerializer, OrderSerializer, OrderItemSerializer


@api_view(['GET', 'PUT', 'POST', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def MenuItemsView(request):
    if request.method == 'GET':
        queryset = MenuItem.objects.all()
        serializer = MenuItemSerializer(queryset, many=True)
        return Response(serializer.data)

    if request.method == 'POST' and request.user.groups.filter(name='Manager').exists():
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"message": "403 Error - Unauthorized action."}, status=status.HTTP_403_FORBIDDEN)

@api_view(['GET', 'PUT', 'POST', 'PATCH', 'DELETE'])
def SingleMenuItemView(request, pk):
    menu_item = get_object_or_404(MenuItem, pk=pk)
    if request.method == 'GET':
        serialized_item = MenuItemSerializer(menu_item)
        return Response(serialized_item.data)

    if request.method == 'PUT' or request.method == 'PATCH':
        if request.user.groups.filter(name='Manager').exists():
            serializer = MenuItemSerializer(menu_item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE' and request.user.groups.filter(name='Manager').exists():
        menu_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response({"message": "403 Error - Unauthorized action."}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def CartView(request):
    cart = Cart.objects.filter(user=request.user)
    if request.method == 'GET':
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
    # Add menu item to the cart
        serializer = CartSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        # Delete all menu items in the cart
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def ManagerView(request):
    if not request.user.groups.filter(name='Manager').exists():
        return Response({"message": "403 Error - Unauthorized user. Please login with a manager account."}, status=status.HTTP_403_FORBIDDEN)

    managers = Group.objects.get(name='Manager').user_set
    if request.method == 'GET':
        serialized_managers = UserSerializer(managers, many=True)
        return Response(serialized_managers.data)

    if request.method == 'POST':
        username = request.data['username']
        if not username:
            return Response({'message': 'Please provide the username to add.'}, status.HTTP_404_NOT_FOUND)

        user = get_object_or_404(User, username=username)
        managers.add(user)
        return Response({'message': 'Added to manager group.'},status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def ManagerDeleteView(request, pk):
    managers = Group.objects.get(name='Manager').user_set
    if request.method == 'DELETE':
        if not pk:
            return Response({'message': 'Please enter the userId in the endpoint to delete.'}, status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(User, pk=pk)
        managers.remove(user)
        return Response({'message': 'Deleted from manager group.'}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def DeliveryView(request):
    if not request.user.groups.filter(name='Manager').exists():
        return Response({"message": "403 Error - Unauthorized user. Please login with a manager account."}, status=status.HTTP_403_FORBIDDEN)

    delivery_crew = Group.objects.get(name='Delivery crew').user_set
    if request.method == 'GET':
        serialized_data = UserSerializer(delivery_crew, many=True)
        return Response(serialized_data.data)

    if request.method == 'POST':
        username = request.data['username']
        if not username:
            return Response({'message': 'Please provide the username to add.'}, status.HTTP_404_NOT_FOUND)

        user = get_object_or_404(User, username=username)
        delivery_crew.add(user)
        return Response({'message': 'Added to delivery crew.'},status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeliveryDeleteView(request, pk):
    delivery_crew = Group.objects.get(name='Delivery crew').user_set
    if request.method == 'DELETE':
        if not pk:
            return Response({'message': 'Please enter the userId in the endpoint to delete.'}, status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(User, pk=pk)
        delivery_crew.remove(user)
        return Response({'message': 'Deleted from delivery crew.'}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def OrderView(request):
    user = request.user
    if request.method == 'GET':
        order = Order.objects.filter(user=user)
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST': 
        cart_items = Cart.objects.filter(user=user)
        if not cart_items:
            return Response({'message': 'Cart empty!'}, status=status.HTTP_200_OK)

        total = sum(item.price for item in cart_items)
        # 1. create an order and save
        # print(cart_items)
        order = {
            'user': user.id,
            'total': total,
        }
        print(order)
        serialized_order = OrderSerializer(data=order)
        print(serialized_order)

        print("<<< 1 <<<")
        serialized_order.is_valid(raise_exception=True)
        order_obj = serialized_order.save()
        print("<<< 3 <<<")
        # 2. add cart items to order items, referencing order.id. and save
        for item in cart_items:
            order_item = model_to_dict(item)
            del order_item['user']
            order_item['order'] = order_obj.id
            serialized_order_item = OrderItemSerializer(data=order_item)
            serialized_order_item.is_valid(raise_exception=True)
            serialized_order_item.save()
        # cart_items.delete()
        return Response(serialized_order.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def SingleOrderView(request, pk):
    pass
