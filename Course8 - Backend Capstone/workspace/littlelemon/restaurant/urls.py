from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.home, name='home'),
    path('bookings/', views.BookingView.as_view({'get': 'list', 'post': 'retrieve'})),
    path('menu/', views.MenuItemview.as_view(), name="menu"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('message/', views.msg),
]
