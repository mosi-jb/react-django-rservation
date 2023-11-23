from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import OTPRequest, User
from user.serializers.front import RequestOTPSerializer, RequestOTPResponseSerializer, VerifyOtpRequestSerializer, \
    ObtainTokenSerializer, UserSerializer


class OTPView(APIView):
    def get(self, request):
        serializer = RequestOTPSerializer(data=request.query_params)
        if serializer.is_valid():
            data = serializer.validated_data
            try:
                otp = OTPRequest.objects.generate(data)
                return Response(data=RequestOTPResponseSerializer(otp).data)
            except Exception as e:
                print(e)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def post(self, request):
        serializer = VerifyOtpRequestSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            if OTPRequest.objects.is_valid(data['receiver'], data['request_id'], data['password']):
                return Response(self._handle_login(data))
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def _handle_login(self, otp):
        User = get_user_model()
        query = User.objects.filter(username=otp['receiver'])
        if query.exists():
            created = False
            user = query.first()
        else:
            user = User.objects.create(username=otp['receiver'])
            created = True

        refresh = RefreshToken.for_user(user)

        return ObtainTokenSerializer({
            'refresh': str(refresh),
            'token': str(refresh.access_token),
            'created': created
        }).data


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewById(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
