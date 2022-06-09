from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserMember(models.Model):
    user_name = models.CharField(max_length=25,unique=True)
    user_email = models.EmailField()
    user_guest = models.IntegerField()
    user_event = models.CharField(max_length=255)
    user_time = models.DateTimeField(max_length=255)
    user_budget = models.IntegerField()
    user_venue = models.CharField(max_length=255)
    user_phone = models.IntegerField()
    user_event = models.CharField(max_length=255)

    user_discription= models.CharField(max_length=255)

    
    def __str__(self):
        return self.user.username


        



