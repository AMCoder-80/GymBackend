from django.urls import path
from base.accounts.views import (
    UserCreationView, ProfileCreationView,
    LoginRequestView
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

    # ---------------------------------------------------------
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]