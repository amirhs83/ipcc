from django.db import models

# Create your models here.
class MyModel(models.Model):
    pass




class Date(models.Model):
    name =models.CharField(max_length=10)



    def __str__(self):
        return self.name





