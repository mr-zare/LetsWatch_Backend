from base64 import urlsafe_b64encode
from django.utils.encoding import force_bytes, force_str


from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.http import JsonResponse
from django.urls import reverse_lazy
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SignupSerializer, ForgotPasswordSerializer, ChangePasswordSerializer

from users.models import CustomUser



class SignupAPIView(generics.CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = (AllowAny, )

class ForgotPasswordAPIView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = CustomUser.objects.filter(email=email).first()
            if user is not None:
                form = PasswordResetForm({'email': email})
                if form.is_valid():
                    subject = 'Password reset'
                    message = 'Please reset your password by clicking on the following link: {0}'.format(
                        request.build_absolute_uri(reverse_lazy('password_reset_confirm', kwargs={
                            'uidb64': urlsafe_b64encode(force_bytes(user.pk)).decode(),
                            'token': default_token_generator.make_token(user),
                        }))
                    )
                    send_mail(subject, message, 'admin@example.com', [email], fail_silently=False)
                return Response({'detail': 'Password reset email has been sent.'})
            else:
                return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            old_password = serializer.data.get('old_password')
            if not user.check_password(old_password):
                return Response({'old_password': ['Wrong password.']}, status=status.HTTP_400_BAD_REQUEST)
            new_password = serializer.data.get('new_password')
            confirm_new_password = serializer.data.get('confirm_new_password')
            if new_password != confirm_new_password:
                return Response({'confirm_new_password': ['Passwords must match.']}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(new_password)
            user.save()
            return Response({'detail': 'Password has been changed.'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'detail': 'Successfully logged out.'})


# Create your views here.
