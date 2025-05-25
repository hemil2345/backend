from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Booking, Contact, UserProfile

class RegisterSerializer(serializers.ModelSerializer):
    dob = serializers.DateField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'dob']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
        }

    def create(self, validated_data):
        dob = validated_data.pop('dob')
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, dob=dob)
        return user


class BookingSerializer(serializers.ModelSerializer):
    # user field is read-only, showing username
    user = serializers.ReadOnlyField(source='user.username')
    # price calculated on server, so read-only
    price = serializers.ReadOnlyField()

    class Meta:
        model = Booking
        fields = [
            'id', 'user', 'sport', 'date', 'start_time', 'duration',
            'is_confirmed', 'price', 'created_at',
            'full_name', 'email', 'phone'
        ]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
