from django.db import models


# Create your models here.


class people(models.Model):
    name = models.CharField(max_length = 255)
    age = models.CharField(max_length = 3)
    phone = models.CharField(max_length = 10)

    def __str__(self):
        return self.name

