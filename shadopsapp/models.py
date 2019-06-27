from django.db import models

# Create your models here.
class LineOfBusiness(models.Model):
    name = models.CharField(max_length = 50, unique=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    country = models.CharField(max_length = 50, blank=False)
    city = models.CharField(max_length = 50, blank=False)
    building = models.CharField(max_length = 50, blank=False)

class DesiredInfo(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    lob = models.ForeignKey(LineOfBusiness, on_delete=models.CASCADE)
    language = models.CharField(max_length = 50, blank=True)

class Employee(models.Model):
    firstName = models.CharField(max_length = 20, blank=False)
    surname = models.CharField(max_length = 20, blank=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    lob = models.ForeignKey(LineOfBusiness, on_delete=models.CASCADE)
    language = models.CharField(max_length = 50, blank=False)
    desiredInfo = models.ForeignKey(DesiredInfo, on_delete=models.CASCADE)
