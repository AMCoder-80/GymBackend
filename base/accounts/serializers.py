from rest_framework import serializers
from base.models import User, Profile
from base.utils.exceptions import CustomException
from rest_framework import status
from base.utils.caching import CachingProcedureHandler
from base.utils.constants import Constant
from base.utils.emails import EmailHandler


class UserCreationSerializer(serializers.ModelSerializer):
    """ Create user serializer """
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class ProfileCreationSerializer(serializers.ModelSerializer):
    """ Create user profile serializer """
    BMI = serializers.FloatField(read_only=True)
    user = UserCreationSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ("age", "weight", "height",
                  "avatar", "description", "user", "BMI")

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


class LoginRequestSerializer(serializers.Serializer):
    """ Serializer for login request """
    email = serializers.EmailField()

    def validate(self, attrs):
        
        try:
            User.objects.get(email=attrs['email'])
        except User.DoesNotExist:
            raise CustomException(
                "user with this email does not exists",
                "error",
                status.HTTP_401_UNAUTHORIZED
            )
        return super().validate(attrs)
    
    def send_token(self):
        """ generate token, store it in cache and sent it via email """
        caching_handler = CachingProcedureHandler()
        email_handler = EmailHandler()
        email = self.data['email']
        token = caching_handler.generate_token()
        result = caching_handler.set_key(
            Constant.LOGIN_TYPE_CACHING,
            email,
            token
        )
        if not result:
            raise CustomException(
                "failed to store token",
                "error",
                status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        email_handler.send_otp(email, token)
        

class VerifyTokenSerializer(serializers.Serializer):
    """ Get token from user and validate it """
    token = serializers.CharField()

    def validate(self, attrs):
        """ validate user token """
        caching_handler = CachingProcedureHandler()
        token = attrs['token']
        email = caching_handler.get_key(Constant.LOGIN_TYPE_CACHING, token)
        if email is None:
            raise CustomException(
                "invalid token",
                "error",
                status.HTTP_403_FORBIDDEN
            )
        attrs.update({
            "email": email
        })
        return attrs
    
    def get_user(self):
        email = self.validated_data['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise CustomException(
                "requested user does not exists",
                "error",
                status.HTTP_400_BAD_REQUEST
            )
        return user