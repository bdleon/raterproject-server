from django.db import models




class GameReview(models.Model):
    review= models.TextField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)