from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=64)
    wait_time = models.CharField(max_length=8)

    class Meta:
        managed = True
