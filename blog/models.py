from django.db import models
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    details=models.TextField()
    date=models.DateField(auto_now_add=True)
    pic=models.FileField(upload_to='files', default='bg_def.jpg')

    def __str__(self):
        return self.title

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    message=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    comment=models.TextField()
    date=models.DateField(auto_now_add=True)
    post=models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.name



