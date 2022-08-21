from django.utils import timezone
from django.db import models

# Create your models here.
class RegisterUser(models.Model):
  id = models.IntegerField(primary_key=True)
  username =  models.TextField(max_length=30)
  email = models.EmailField(max_length=30, default="")
  password = models.TextField(max_length=30)
  date = models.DateField(timezone.now)

  def __str__(self):
    return (self.username)

class Post(models.Model):   
  id = models.IntegerField(primary_key=True)
  title = models.TextField(max_length=30)
  date_posted = models.DateField(auto_now_add=True)
  description = models.TextField(max_length=30)
  image_file = models.FileField(upload_to="media/pics/", default="")
  #author = models.ForeignKey(RegisterUser, on_delete=models.CASCADE, default="")

  def __str__(self):
    return (self.title)
