from django.contrib import admin
from .models import DrinksCategory, Drinks, Booking, Employees, Menu

admin.site.register([DrinksCategory, Drinks, Booking, Employees, Menu])
