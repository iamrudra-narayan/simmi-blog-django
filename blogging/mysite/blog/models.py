from django.db import models

# Create your models here.
class User(models.Model):
  id = models.AutoField(primary_key=True)
  username =  models.TextField(max_length=30)
  password = models.TextField(max_length=30)
  date = models.DateField(auto_now_add=True)

  def __str__(self):
    return (self.username)