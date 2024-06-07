from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import update_last_login


def generate_token_for_user(user):
    """ Generate access and refresh token for user """
    tokens = RefreshToken.for_user(user)
    update_last_login(None, user)
    response = {
        'refresh': str(tokens),
        'access': str(tokens.access_token),
        'has_profile': hasattr(user, 'profile')
    }
    return response