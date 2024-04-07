from django.db import models

# Create your models here.

class Train(models.Model) :
    trainID = models.AutoField(primary_key=True)
    to = models.CharField(max_length = 20)
    time = models.CharField(max_length = 20)
    voie = models.IntegerField()