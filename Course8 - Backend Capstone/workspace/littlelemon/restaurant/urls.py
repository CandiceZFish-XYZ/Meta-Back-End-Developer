from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menuView.as_view()),
    path('bookings/', views.bookingView.as_view()),
]
