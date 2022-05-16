from django.db import models

# Create your models here.

class Asset(models.Model):
    Aid = models.CharField(max_length=20)
    Aname = models.CharField(max_length=50)
    Atype = models.CharField(max_length=50)
    Adestination = models.CharField(max_length=100)

    def __str__(self):
         return "%s " %(self.Aname)

    class Meta:
        db_table = "AssetRegistration"