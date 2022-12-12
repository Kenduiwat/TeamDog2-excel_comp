from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    phone_number = models.CharField(max_length=50, default='')
    Birthday = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    school = models.CharField(max_length=100, default='')
    course = models.CharField(max_length=50, default=''