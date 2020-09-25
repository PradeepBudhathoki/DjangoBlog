from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #user and posts are going to have one to many relationships;user
#user is already a model created by django
from django.urls import reverse


class Post(models.Model):#a table in the database
    title = models.CharField(max_length=100)# attribute of table
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #deletepost if userdeleted not viceversa

    def __str__(self):
        return self.title

    #creating 'get absolute url' method
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})


    



