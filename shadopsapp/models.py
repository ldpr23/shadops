from django.db import models

# Create your models here.
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
 
