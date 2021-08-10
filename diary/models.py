from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=30)
    published_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
