from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    age = models.CharField(max_length=2)
    password = models.CharField(max_length=50,null=True)
    date = models.DateField()
    def __str__(self):
        return self.name