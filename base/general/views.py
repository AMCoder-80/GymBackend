from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from base.general.serializers import WorkoutGifListSerializer
from base.models import WorkoutGif


class WorkoutGifListView(ListAPIView):
    """ List all objects """
    serializer_class = WorkoutGifListSerializer
    queryset = WorkoutGif.objects.all()
