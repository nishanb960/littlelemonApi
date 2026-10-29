from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request, 'index.html')


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]
    
    
class SingleMenuItemsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]
    

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

@api_view (["GET"])
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({
        "message" : "This message is protected"
    })