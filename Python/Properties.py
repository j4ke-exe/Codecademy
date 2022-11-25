class Box:
 def __init__(self, weight):
   self.__weight = weight
 
 @property
 def weight(self):
   """Docstring for the 'weight' property"""
   return self.__weight
 
 
 @weight.setter
 def weight(self, weight):
   if weight >= 0:
     self.__weight = weight
 
 @weight.deleter
 def weight(self):
   del self.__weight
