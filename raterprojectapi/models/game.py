from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    designer = models.CharField(max_length=50)
    year_released = models.CharField(max_length=15)
    num_of_players = models.IntegerField()
    estimated_time_to_play = models.IntegerField()
    age_recommendation = models.CharField(max_length=20)