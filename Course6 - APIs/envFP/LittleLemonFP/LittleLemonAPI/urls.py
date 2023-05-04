from django.urls import path, include
from . import views

urlpatterns = [
    path('menu-items/', views.MenuItemsView),
    path('menu-items/<int:pk>/', views.SingleMenuItemView),
    path('cart/menu-items/', views.CartView),
    path('secret/', views.secret),
]
