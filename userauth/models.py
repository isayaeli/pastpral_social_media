from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    WORK_TYPE = (
        ('Full Time', 'Full Time'),
         ('Part Time', 'Part Time')
    )
    PROFILE_TYPE =(
        ('officer','officer'),
        ('farmer', 'farmer')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    work_type = models.CharField(choices=WORK_TYPE, max_length=100)
    image = models.ImageField(upload_to='profile_images')
    profile_type = models.CharField(choices=PROFILE_TYPE, max_length=100)