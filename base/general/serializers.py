from rest_framework import serializers
from base.models import WorkoutGif, Client, Exercise
import uuid


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


class ExerciseListSerializer(serializers.ModelSerializer):
    """ List all exercises """
    status = serializers.SerializerMethodField(method_name="get_status")
    type = serializers.SerializerMethodField(method_name="get_type")
    class Meta:
        model = Exercise
        fields = ("id", "title", "repeatation", "duration", "status", "type", "image")
    
    def get_status(self, obj):
        return obj.get_status_display()

    def get_type(self, obj):
        return obj.get_type_display()
    

class CreateExerciseSerializer(serializers.ModelSerializer):
    """ create a new object with some fields """
    class Meta:
        model = Exercise
        fields = ("title", "type", "token")
        read_only_fields = ('token', )
    
    def create(self, validated_data):
        unique_value = str(uuid.uuid4())
        request = self.context['request']
        obj = Exercise.objects.create(
            token=unique_value,
            profile=request.user.profile,
            image=f"exercise_images/{validated_data['type']}.jpeg",
            **validated_data
        )
        return obj