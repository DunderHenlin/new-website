from django.db import models

class Blog(models.Model):
    Title= models.CharField(max_length=100)
    Date=models.DateField()
    Description=models.CharField(max_length=250)


    def __str__(self):
        return self.Title