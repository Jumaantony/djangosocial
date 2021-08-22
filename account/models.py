from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    photo = CloudinaryField('image', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'