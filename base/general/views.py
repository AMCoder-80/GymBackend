from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView
from base.general.serializers import (
    WorkoutGifListSerializer, ClientListSerializer,
    CreateExerciseSerializer, ExerciseListSerializer
    )
from base.models import WorkoutGif, Client, Exercise


class WorkoutGifListView(ListAPIView):
    """ List all objects """
    serializer_class = WorkoutGifListSerializer
    queryset = WorkoutGif.objects.all()


class ClientListSerializer(ListAPIView):
    """ List all objects """
    serializer_class = ClientListSerializer
    queryset = Client.objects.all()


class ExerciseCreateListView(ListCreateAPIView):
    """ List and create objects """
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateExerciseSerializer
        elif self.request.method == 'GET':
            return ExerciseListSerializer
    
    def get_queryset(self):
        return Exercise.objects.filter(
            profile=self.request.user.profile
        )