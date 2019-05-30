from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    
    bio = models.TextField(max_length=200, null=True, blank=True, default="bio")
    profile_pic = models.ImageField(upload_to='profile_picture/', null=True, blank=True, default= 0)
    user= models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="profile")
    contact=models.IntegerField(default=0)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

        post_save.connect(create_user_profile, sender=User)


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


    @classmethod
    def search_users(cls, search_term):
        profiles = cls.objects.filter(user__username__icontains=search_term)
        return profiles

    @property
    def image_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url

    def __str__(self):
        return self.user.username


class Project(models.Model):
    title = models.TextField(max_length=200, null=True, blank=True, default="title")
    project_image = models.ImageField(upload_to='picture/', null=True,)
    description = HTMLField()
    project_url=models.URLField(max_length=250)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    profile=models.ForeignKey(Profile, null=True)

    def save_project(self):
        self.save()

    @classmethod
    def delete_project_by_id(cls, id):
        projects = cls.objects.filter(pk=id)
        projects.delete()

    @classmethod
    def get_project_by_id(cls, id):
        projects = cls.objects.get(pk=id)
        return projects

    @classmethod
    def search_projects(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects


    def __str__(self):
        return self.title


