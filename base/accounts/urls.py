from django.urls import path
from base.accounts.views import (
    UserCreationView, ProfileCreationView,
    LoginRequestView, VerifyTokenView,
    UpdateProfileView
    )

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path('signup/', UserCreationView.as_view(), name='create_user'),
    path('profile/create/', ProfileCreationView.as_view(), name='create_profile'),
    path('signin/', LoginRequestView.as_view(), name='login_request'),
    path('verify-token/', VerifyTokenView.as_view(), name='verify_OTP'),
    path('profile/', UpdateProfileView.as_view(), name='update_profile'),

    # ---------------------------------------------------------
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]