from django.db import models

# Create your models here.

#the models.Model says we're extending the regular model class that Django has and we're adding our own special fiels
#this means for every post we create on the blog, we can give it a title, date, etc
class Post(models.Model):
    #for the char field, you need a parameter for the max_length
    title = models.CharField(max_length=100)
    date = models.DateField()
    content = models.TextField()