from django.db import models
from base.models import BaseModel


class WorkoutGif(BaseModel):
    """ Store each gif and its creation date """
    gif = models.FileField(upload_to="gifs/")

    def __str__(self):
        return f"WorkoutGif Object: {self.id}"


class ExerciseStatusChoices(models.TextChoices):
    """ choices for different status """
    CREATED = 'created', 'Created'
    DOING = 'doing', 'Doing'
    DONE  = 'done', 'Done'


class ExerciseTypeChoices(models.TextChoices):
    """ Choices about what is the meaning each exercise type """
    PUSH_UP = 'push_up', 'Push Up'
    PULL_UP = 'pull_up', 'Pull Up'
    PLANK = 'plank', 'Plank'
    SQUAT = 'squat', 'Squat'
    CRUNCH = 'crunch', 'Crunch'


class Exercise(BaseModel):
    """ Store each exercise which is done by user """
    title = models.CharField(max_length=50)
    token = models.UUIDField()
    type = models.CharField(max_length=10, choices=ExerciseTypeChoices.choices)
    status = models.CharField(max_length=10, choices=ExerciseStatusChoices.choices, default=ExerciseStatusChoices.CREATED.value)

    # Numerical fields
    repeatation = models.PositiveSmallIntegerField(blank=True, null=True)
    duration = models.PositiveSmallIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='exercise_images/', null=True, blank=True)

    # Relational fields
    profile = models.ForeignKey('base.Profile', on_delete=models.CASCADE, related_name="exercises")

    def __str__(self):
        return f"Exercise Object: {self.id} - {self.get_status_display()} - {self.get_type_display()}"
    

class Client(BaseModel):
    """ What clients say """
    # Textual fields
    name = models.CharField(max_length=100)
    opinion = models.TextField()

    # Image fields
    image = models.ImageField(upload_to="clients_avatar/")

    def __str__(self):
        return f"Client Object: {self.id} - {self.name}"