# Django related modules

# DRF related modules
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

# Local modules
from base.accounts.serializers import UserCreationSerializer
from base.models import User
from base.utils.auth import generate_token_for_user


# @api_view(['POST'])
# def create_user(request):
#     """ Create a new user """
#     if request.method == 'POST':
#         serialized = UserCreationSerializer(data=request.data)
#         serialized.is_valid(raise_exception=True)
#         serialized.save()
#         return Response(serialized.data, status=status.HTTP_201_CREATED)


class UserCreationView(GenericAPIView):
    """ Create a new user """
    serializer_class = UserCreationSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serialized = self.get_serializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        user = serialized.save()
        
        response = generate_token_for_user(user)

        return Response(response, status=status.HTTP_201_CREATED)