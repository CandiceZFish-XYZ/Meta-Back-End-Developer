from django.shortcuts import render
from django.urls import is_valid_path
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Booking, Menu
from .serializers import bookingSerializer, menuSerializer

def home(request):
    return render(request, 'index.html', {})

class bookingView(APIView):
    def get(self, request):
        items = Booking.objects.all()
        serializer = bookingSerializer(items, many=True)
        return Response(serializer.data) # return JSON

    def post(self, request):
        serializer = bookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})

class menuView(APIView):
    def get(self, request):
        items = Menu.objects.all()
        serializer = menuSerializer(items, many=True)
        return Response(serializer.data) # return JSON

    def post(self, request):
        serializer = menuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
