from rest_framework import serializers
from base.models import User


class UserCreationSerializer(serializers.ModelSerializer):
    """ Create user serializer """
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
