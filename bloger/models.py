from django.db import models

# Create your models here.
class Admin(models.Model):
    full_name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    pic=models.FileField(upload_to='bloger_pic', default='avtar.png')

    def __str__(self):
        return self.full_name


