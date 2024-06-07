from rest_framework import serializers
from base.models import User, Profile
from base.utils.exceptions import CustomException
from rest_framework import status


class UserCreationSerializer(serializers.ModelSerializer):
    """ Create user serializer """
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class ProfileCreationSerializer(serializers.ModelSerializer):
    """ Create user profile serializer """
    class Meta:
        model = Profile
        fields = ("age", "weight", "height", "avatar", "description")

    def validate(self, attrs):
        
        request = self.context['request']
        user = request.user

        profiles = Profile.objects.filter(user=user)
        if profiles.exists():
            raise CustomException(
                "you already have a profile object",
                "error",
                status.HTTP_400_BAD_REQUEST
            )
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        user = self.context['request'].user
        weight = validated_data['weight']
        height = validated_data['height']
        BMI = round(weight / (height / 100)**2, 1)
        profile = Profile.objects.create(
            user=user,
            BMI=BMI,
            **validated_data
        )
        print(profile)
        return profile
