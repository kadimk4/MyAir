from django.db import models

class Plane(models.Model):
    code = models.CharField(max_length=15, unique=True)

class Plane_Attribute(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
class Plane_Value(models.Model):
    attribute_id = models.ForeignKey(Plane_Attribute, on_delete=models.CASCADE)
    plane_id = models.ForeignKey(Plane, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)
