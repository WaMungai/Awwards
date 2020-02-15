from django.test import TestCase
from .models import Project,Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.newuser=User(username='clover')
        self.newuser.save()
        self.biography=Profile(profile_photo='pic.jpg',bio='mandem',contact='0712345678',editor=self.newuser)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.biography,Profile))
        
    def test_save_profile(self):
        self.biography.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)
        
    def test_delete_profile(self):
        self.biography.save_profile()
        self.biography.delete_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)==0)
        
    def test_get_profile(self):
        self.biography.save_profile()
        firstprofile=Profile.get_profile()
        self.assertTrue(firstprofile is not None)

class ProjectTestClass(TestCase):
    def setUp(self):
        self.newuser=User(username='clover')
        self.newuser.save()
        self.projects=Project(title='code',image='img.jpg',description='icodeinheels',editor=self.newuser)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.projects,Project))
        
    def test_save_project(self):
        self.projects.save_project()
        allprojects=Project.objects.all()
        self.assertTrue(len(allprojects)>0)
        
    def test_delete_projects(self):
        self.projects.save_project()
        self.projects.delete_project()
        allprojects=Project.objects.all()
        self.assertTrue(len(allprojects)==0)
        
    def test_get_projects(self):
        self.projects.save_project()
        firstproject=Project.get_projects()
        self.assertTrue(firstproject is not None)