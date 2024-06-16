from django.urls import path
from base.general.views import (
    WorkoutGifListView, ClientListSerializer,
    ExerciseCreateListView, ExerciseUpdateView
)


urlpatterns = [
    path('workouts/', WorkoutGifListView.as_view(), name="list_all_workouts"),
    path('clients/', ClientListSerializer.as_view(), name="list_all_clients"),
    path('exercise/', ExerciseCreateListView.as_view(), name="list_and_create_exercise"),
    path('exercise/<str:token>/', ExerciseUpdateView.as_view(), name="get_and_update_exercise"),
]