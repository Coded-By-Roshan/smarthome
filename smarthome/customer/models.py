from django.db import models

# Create your models here.

class AudioModel(models.Model):
    audio_text = models.CharField(max_length=100,default=0)
    

    def __str__(self):
        return self.audio_text
