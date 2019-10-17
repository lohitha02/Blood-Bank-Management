from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100, null=True)
    district = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name
