from django.db import models

class GameRating(models.Model):
    rating = models.IntegerField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)