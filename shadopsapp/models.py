from django.db import models

# Create your models here.
class Person():
  def __init__(self, fname, lname, loc, lang, tech, lob):

    # current info about job
    self.fname = fname
    self.lname = lname
    self.lang = lang
    self.tech = tech
    self.lob = lob
    self.loc = loc
      
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
