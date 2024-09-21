from django.db import models

class jobmodel(models.Model):
    type=models.CharField(max_length=100)
    selary=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    logopic=models.ImageField(upload_to='Media/pic',null=True)
    description=models.CharField(max_length=100)

