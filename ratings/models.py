from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='images/',blank=True)
    bio=models.CharField(max_length=100)
    contact=models.CharField(max_length=25)
    editor=models.ForeignKey(User ,on_delete=models.CASCADE)
    
class Project(models.Model):
    title=models.CharField(max_length=30)
    image=models.ImageField(upload_to='images/',blank=True)
    description=HTMLField()
    link=models.URLField(max_length=128,db_index=True,unique=True,blank=True)
    editor=models.ForeignKey(User,on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile,null=True)
    pub_date=models.DateTimeField(auto_now_add=True)
    
class Rating(models.Model):
    editor=models.ForeignKey(User,on_delete=models.CASCADE)
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    design=models.IntegerField()
    usability=models.IntegerField()
    content=models.IntegerField()
    