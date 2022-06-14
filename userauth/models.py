from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class Profile(models.Model):
    WORK_TYPE = (
        ('Full Time', 'Full Time'),
         ('Part Time', 'Part Time')
    )
    PROFILE_TYPE =(
        ('officer','officer'),
        ('pastoralist', 'pastoralist')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    work_type = models.CharField(choices=WORK_TYPE, max_length=100)
    image = models.FileField(upload_to='profile_images',default='avatar.png')
    role = models.CharField(choices=PROFILE_TYPE, max_length=100)
    followers = models.ManyToManyField(User, related_name='followers', blank=True)

    def __str__(self):
        return str(self.user)



def create_profile(sender, **kwargs):
    if kwargs['created']:
       profile = Profile.objects.create(user=kwargs['instance'])
       
post_save.connect(create_profile, sender=User)