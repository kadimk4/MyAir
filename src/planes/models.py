from django.db import models

class Plane_Attribute(models.Model):
    attribute = models.CharField(max_length=100)
    
class Plane_Value(models.Model):
    attribute_id = models.ForeignKey(Plane_Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)
