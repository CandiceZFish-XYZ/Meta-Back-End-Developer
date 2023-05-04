from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

from .models import MenuItem, Cart
from .serializers import MenuItemSerializer, CartSerializer


# from rest_framework import status, generics, serializers
# from rest_framework.views import APIView

@api_view(['GET', 'PUT', 'POST', 'PATCH', 'DELETE'])
def MenuItemsView(request):
    if (request.method == 'GET'):
        queryset = MenuItem.objects.all()
        serializer = MenuItemSerializer(queryset, many=True)
        return Response(serializer.data)
    
    return Response({"message": "403 Error - Unauthorized action."}, status=status.HTTP_403_FORBIDDEN)

@api_view(['GET', 'PUT', 'POST', 'PATCH', 'DELETE'])
def SingleMenuItemView(request, pk):
    if (request.method == 'GET'):
        menu_item = get_object_or_404(MenuItem, pk=pk)
        serialized_item = MenuItemSerializer(menu_item)
        return Response(serialized_item.data)
    
    return Response({"message": "403 Error - Unauthorized action."}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def CartView(request):
    if (request.method == 'GET'):
        cart = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)
    
    if (request.method == 'POST'):
    # Add menu item to the cart
        serializer = CartSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if (request.method == 'DELETE'):
        # Delete all menu items in the cart
        Cart.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
