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

# class Language(models.Model):
#     language = models.CharField(max_length=20, unique=True)
#     slug = models.SlugField(max_length=40, unique=True)

#     class Meta:
#         verbose_name_plural = 'Languages'

#     def __str__(self):
#         return self.name

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super(Language, self).save(*args, **kwargs)

# class Technology(models.Model):
#     technolgy = model.CharField(max_length=30, unique=True)
#     slug = models.SlugField(max_length=40, unique=True)

#     class Meta:
#         verbose_name_plural = 'Technologies'

#     def __str__(self):
#         return self.name

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super(Technology, self).save(*args, **kwargs)

class DesiredInfo(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    lob = models.ManyToManyField(LineOfBusiness, on_delete=models.CASCADE)
    technology = models.ManyToManyField(Technology, on_delete=models.CASCADE)
    language = models.ManyToManyField(Language, on_delete=models.CASCADE)

class Employee(models.Model):
    firstName = models.CharField(max_length = 20, blank=False)
    surname = models.CharField(max_length = 20, blank=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    lob = models.ForeignKey(LineOfBusiness, on_delete=models.CASCADE)
    language = models.ManyToManyField(Language, on_delete=models.CASCADE)
    technology = models.ManyToManyField(Technology, on_delete=models.CASCADE)
    desiredInfo = models.ForeignKey(DesiredInfo, on_delete=models.CASCADE)
