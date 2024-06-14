from django.urls import path
from base.general.views import WorkoutGifListView, ClientListSerializer


urlpatterns = [
    path('workouts/', WorkoutGifListView.as_view(), name="list_all_workouts"),
    path('clients/', ClientListSerializer.as_view(), name="list_all_clients")
]