from django.db import models

class Create_Admin(models.Model):
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=50)
    
    def __str__(self):
        return self.username
     
