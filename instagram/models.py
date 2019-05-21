from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from tinymce.models import HTMLField
import datetime as dt


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20)
    bio = models.TextField(max_length=40)
    profile_pic = models.ImageField(upload_to='profile/', null=True, blank=True)
    followers = models.CharField(max_length = 40, blank = True, default= 0)
    following = models.CharField(max_length = 40, blank = True, default= 0)


    def __str__(self):
        return self.user_name

    def save_profile(self):
        self.save() 

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.update()    

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles

    @classmethod
    def search_by_username(cls,user_name):
        profiles = cls.objects.filter(user_name__icontains=user_name)
        return profiles

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save() 

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=40)
    image_caption = models.CharField(max_length=40, null=True)
    
    Profile = models.ForeignKey(Profile,on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    likes = models.CharField(max_length=40,blank=True,default=0)
    Image_comments = models.CharField(max_length=40,blank=True,default=0)

  

    def save_images(self):
        self.save()    

    @classmethod
    def get_images(cls):

        images = cls.objects.all()
        return images


class Comments(models.Model):
    comments = models.CharField(max_length = 250)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    def delete__comment(self):
        self.delete()

    @classmethod
    def get_comments_by_images(cls, id):
        comments = Comments.object.filter(image__pk = id)
        return comments   

class Like(models.Model):
    photo = models.CharField(max_length=40,default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.user_name  

class Contact(models.Model):
    user_from = models.ForeignKey(User, related_name='rel_from_set')
    user_to = models.ForeignKey(User, related_name='rel_to_set')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to )

    

