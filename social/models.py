from django.db import models
from django.contrib.auth import get_user_model # getting the model of the currently authenticated user
# Create your models here.

User = get_user_model() # initialiting
# creating a model for the profiles that will be registered
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user =  models.IntegerField()
    bio = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(upload_to='profile_images',default='wink.png') # saving the files and setting a default picture
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return {self.user.username}