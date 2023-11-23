from django.urls import path

from user.views.front import OTPView, UserView, UserViewById

urlpatterns = [
    path('otp/', OTPView.as_view(), name='otp_view'),
    path('user/', UserView.as_view()),
    path('user/<pk>', UserViewById.as_view()),
]
