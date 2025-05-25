from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Booking, Contact
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny] 


class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]
    authentication_classes = [] 

    def perform_create(self, serializer):
        duration = serializer.validated_data.get('duration', 1)
        price = duration * 100
        serializer.save(
            price=price,
            full_name=serializer.validated_data.get('full_name'),
            email=serializer.validated_data.get('email'),
            phone=serializer.validated_data.get('phone'),
            user=None  # Optional
        )



class BookingStatusView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    permission_classes = [AllowAny]
    authentication_classes = [] 

    def delete(self, request, *args, **kwargs):
        booking = self.get_object()
        if booking.is_cancellable():
            booking.delete()
            return Response({'message': 'Booking cancelled with 100% refund'}, status=200)
        else:
            return Response({'error': 'Cancellation period expired'}, status=400)

class ContactView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]
