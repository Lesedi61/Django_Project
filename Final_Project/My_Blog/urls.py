from My_Blog.views import homepage, contact, show_titles,vision
from django.urls import path

app_name = 'my_blog'

urlpatterns = [
    path('home', homepage),
    path('vision', vision),
    path('contact', contact),
    path('projects', show_titles),
]