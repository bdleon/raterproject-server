from django.db import models

class GamePictureUpload(models.Model):
    image = models.ImageField(upload_to ='uploads/')
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)