from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, default='')
    body = models.CharField(max_length=500, default='')
    created_at= models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.title
