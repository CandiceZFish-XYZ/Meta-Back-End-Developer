from django.urls import path, include
from . import views

urlpatterns = [
    path('menu-items/', views.MenuItemsView),
    path('menu-items/<int:pk>/', views.SingleMenuItemView),
    path('cart/menu-items/', views.CartView),
    path('groups/manager/users/', views.ManagerView),
    path('groups/manager/users/<int:pk>/', views.ManagerDeleteView),
    path('groups/delivery-crew/users/', views.DeliveryView),
    path('groups/delivery-crew/users/<int:pk>/', views.DeliveryDeleteView),
    path('orders/', views.OrderView),
    path('orders/<int:pk>/', views.SingleOrderView),
]
