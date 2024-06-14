from rest_framework import serializers
from base.models import WorkoutGif


class WorkoutGifListSerializer(serializers.ModelSerializer):
    """ List all objects of workout gif model """
    class Meta:
        model = WorkoutGif
        fields = ("id", "gif")
