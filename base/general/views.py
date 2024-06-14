from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from base.general.serializers import WorkoutGifListSerializer, ClientListSerializer
from base.models import WorkoutGif, Client


class WorkoutGifListView(ListAPIView):
    """ List all objects """
    serializer_class = WorkoutGifListSerializer
    queryset = WorkoutGif.objects.all()


class ClientListSerializer(ListAPIView):
    """ List all objects """
    serializer_class = ClientListSerializer
    queryset = Client.objects.all()