from django.db import models

# Create your models here.
<<<<<<< HEAD
class Person(models.Model):
  def __init__(self, id, fname, lname, loc, lang, tech, lob):

    # current info about job#
    self.id = id
    self.fname = fname
    self.lname = lname
    self.loc = loc
    self.lang = lang
    self.tech = Technology(tech)
    self.lob = lob
      
    # desired info for shadowing
    self.desiredLoc = []
    self.desiredLang = []
    self.desiredTech = []
    self.desiredLob = []

    # setters
    def set_loc(self, desiredLoc): 
        self.desiredLoc = desiredLoc
        
    def set_lang(self, desiredLang): 
        self.desiredLang = desiredLang

    def set_tech(self, desiredTech): 
        self.desiredTech = desiredTech 

    def set_lob(self, desiredLob): 
        self.desiredLob = desiredLob

class Language():
    def __init__(self, lang):
        self.lang = lang

class Tecnology():
    def __init__(self, tech):
        self.tech = tech
 
=======
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
>>>>>>> 5be838323ae355870d5f7532eb97bf29eb34b67a
