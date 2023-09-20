from django.db import models

# Create your models here.



class AudioModel(models.Model):
    audio_text = models.CharField(max_length=100,default=0)
    username  =models.CharField(max_length=100,default=0, null=True,blank=True)
    roomno  =models.CharField(max_length=100,default=0, null=True,blank=True)
    def __str__(self):
        return self.audio_text
    

