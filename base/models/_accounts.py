from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    """ Custom user manager """
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_active"):
            raise ValueError("is_active value is not valid")
        
        if not extra_fields.get("is_staff"):
            raise ValueError("is_staff value is not valid")
        
        if not extra_fields.get("is_superuser"):
            raise ValueError("is_superuser value is not valid")
        
        return self.create_user(email, password, **extra_fields)
        
    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_active", True)
        if not extra_fields.get("is_active"):
            raise ValueError("is_active value is not valid")
        
        try:
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save()
            return user
        except Exception as e:
            print(e)
            raise ValueError(e)



class User(AbstractBaseUser, PermissionsMixin):
    """ main model for storing user information """
    # Personal information
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    # django related fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # date and time related fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return f"User Object: {self.id} - {self.get_full_name()}"


class Profile(models.Model):
    """ Store platform related data for each user """
    # Numberical fields
    age = models.PositiveIntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    BMI = models.FloatField()

    # Image related fields
    avatar = models.ImageField(upload_to='user_avatar/')

    # Textual fields
    description = models.TextField(blank=True, null=True)

    # Relational fields
    user = models.OneToOneField("base.User", on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return f"Profile Object: {self.id} - {self.user.get_full_name()}"