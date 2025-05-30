from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('booking/', BookingView.as_view()),
    path('booking/<int:pk>/', BookingStatusView.as_view()),
    path('contact/', ContactView.as_view()),
    
]
