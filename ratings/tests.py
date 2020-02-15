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
