from django.db import models

# Create your models here.
class student(models.Model):
    username = models.CharField(null=True,blank=True,max_length=40)
    age = models.IntegerField(null=True,blank=True)
    email = models.CharField(null=True,blank=True,max_length=40)

    def __str__(self):
        return self.username