from rest_framework import serializers
from base.models import WorkoutGif, Client


class WorkoutGifListSerializer(serializers.ModelSerializer):
    """ List all objects of workout gif model """
    class Meta:
        model = WorkoutGif
        fields = ("id", "gif")


class ClientListSerializer(serializers.ModelSerializer):
    """ List what clients say """
    class Meta:
        model = Client
        fields = ("id", "name", "opinion", "image")
