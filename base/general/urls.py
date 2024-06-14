from django.urls import path
from base.general.views import WorkoutGifListView


urlpatterns = [
    path('workouts/', WorkoutGifListView.as_view(), name="list_all_workouts")
]