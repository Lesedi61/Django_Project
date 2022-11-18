from atexit import register
from django.contrib import admin
from My_Blog.models import Article, Article, Topic
# Register your models here.

admin.site.register(Topic)
admin.site.register(Article)
