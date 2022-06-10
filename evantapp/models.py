from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserMember1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_email = models.EmailField()
    user_guest = models.IntegerField()
    user_event = models.CharField(max_length=255)
    user_time = models.DateTimeField(max_length=255)
    user_budget = models.IntegerField()
    user_venue = models.CharField(max_length=255)
    user_phone = models.IntegerField()
    user_event = models.CharField(max_length=255)
    status = models.CharField(max_length=255,default="0")
    user_discription= models.CharField(max_length=255)

    
    def __str__(self):
        return self.user.username


class UserMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_email = models.EmailField()
    
    
    def __str__(self):
        return self.user.username

        



