from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Profile(models.Model):
  bio = models.TextField(max_length=200, blank=True)
  photo = models.CharField(max_length=200, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"Profile for user: {self.user.first_name} at user_id {self.user_id}."

class Restaurant(models.Model):
  name = models.TextField(max_length=100)
  location = models.TextField(max_length=300, blank=True)
  phone = models.TextField(max_length=15, blank=True)
  website = models.TextField(max_length=200, blank=True)
  creator = models.TextField(max_length=100, blank=True)
  
  def __str__(self):
    return f"This is restaurant: {self.name}"

class Note(models.Model):
  date = models.DateField(default=datetime.now)
  content = models.TextField(max_length=500)
  restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.content} on {self.date}"

  class Meta:
    ordering = ['-date']
