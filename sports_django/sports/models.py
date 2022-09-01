from django.db import models

# Create your models here.
class Team(models.Model):
     name = models.CharField(max_length=100)
     city = models.CharField(max_length=100)
     league = models.CharField(max_length=100)
     photo_url = models.TextField()

     def __str__(self):
        return self.name

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='teams')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    injured = models.BooleanField()

    def __str__(self):
        return self.name