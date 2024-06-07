from django.urls import path
from base.accounts.views import UserCreationView


urlpatterns = [
    path('signup/', UserCreationView.as_view(), name='create_user')
]