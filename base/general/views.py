from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from base.general.serializers import (
    WorkoutGifListSerializer, ClientListSerializer,
    CreateExerciseSerializer, ExerciseListSerializer,
    ExerciseUpdateSerializer
    )
from base.models import WorkoutGif, Client, Exercise
from base.utils.permissions import HasProfile


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
    permission_classes = (HasProfile, )

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateExerciseSerializer
        elif self.request.method == 'GET':
            return ExerciseListSerializer
    
    def get_queryset(self):
        return Exercise.objects.filter(
            profile=self.request.user.profile
        )


class ExerciseUpdateView(RetrieveUpdateAPIView):
    """ Return and update a single exercise object """
    serializer_class = ExerciseUpdateSerializer
    queryset = Exercise.objects.all()
    permission_classes = (HasProfile, )
    lookup_field = 'token'