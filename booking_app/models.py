from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()

    def __str__(self):
        return self.user.username

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

class Booking(models.Model):
    SPORT_CHOICES = (('cricket', 'Cricket'), ('bowling', 'Bowling'))

    # Allow user to be optional
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    sport = models.CharField(max_length=10, choices=SPORT_CHOICES)
    date = models.DateField()
    start_time = models.TimeField()
    duration = models.PositiveIntegerField()
    is_confirmed = models.BooleanField(default=False)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    full_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def is_cancellable(self):
        from datetime import datetime, timedelta
        return (datetime.now() - self.created_at.replace(tzinfo=None)) <= timedelta(hours=24)