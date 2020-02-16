from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='images/',blank=True)
    bio=models.CharField(max_length=100)
    contact=models.CharField(max_length=25)
    editor=models.ForeignKey(User ,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title 
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
    
    @classmethod   
    def get_profile(cls):
        profile=cls.objects.all()
        return profile
    
class Project(models.Model):
    title=models.CharField(max_length=30)
    image=models.ImageField(upload_to='images/',blank=True)
    description=HTMLField()
    link=models.URLField(max_length=128,db_index=True,unique=True,blank=True)
    editor=models.ForeignKey(User,on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile,null=True)
    pub_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def save_project(self):
        self.save()
        
    def delete_project(self):
        self.delete()
        
    @classmethod
    def get_projects(cls):
        project=cls.objects.all()
        return project
    
    @classmethod
    def search_by_title(cls,tag):
        search_result=cls.objects.filter(title__icontains=tag)
        return search_result
    
    @classmethod
    def user_projects(cls,user_id):
        project_posted=cls.objects.ger(editor=user_id)
        return project_posted
    
    @classmethod
    def single_project(cls,project_id):
        projects_posted=cls.objects.get(id=project_id)
        return projects_posted
    
    @classmethod
    def get_image_id(cls,imageId):
        image_id=cls.objects.filter(id=imageId)
        return image_id 
        
        
class Rating(models.Model):
    editor=models.ForeignKey(User,on_delete=models.CASCADE)
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    design=models.IntegerField()
    usability=models.IntegerField()
    content=models.IntegerField()
    