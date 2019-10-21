from django.db import models


class Coord(models.Model):
    lon = models.FloatField(default=0)
    lat = models.FloatField(default=0)


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=20)
    ow_id = models.IntegerField(default=0)
    coord = models.OneToOneField(
        Coord,
        on_delete=models.CASCADE,
        primary_key=True,
    )



 


