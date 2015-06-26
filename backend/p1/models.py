from django.db import models

# Create your models here.
class TmpAuth(models.Model):
    username = models.CharField(max_length=30)
    tmpcode = models.IntegerField()