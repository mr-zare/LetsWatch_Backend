from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ForgotPasswordAPIView, ChangePasswordAPIView, LogoutAPIView, EditProfileView, LoginAPIView, \
    SignUpAPIView
from . import views

# from .views import CustomPasswordResetView

urlpatterns = [
    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('forgot-password/', ForgotPasswordAPIView.as_view(), name='forgot_password'),
    path('change-password/', ChangePasswordAPIView.as_view(), name='change_password'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('editprofile/<int:pk>', EditProfileView.as_view(), name='editprofile'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]
