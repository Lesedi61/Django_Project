from email.policy import default
from multiprocessing.sharedctypes import Value
from statistics import mode
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Topic(models.Model):
    project_topic = models.CharField(max_length = 256)

    def __str__(self):
        return self.project_topic

class Article(models.Model):

    title = models.CharField(max_length = 256)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name= 'articles')
    article = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

   

