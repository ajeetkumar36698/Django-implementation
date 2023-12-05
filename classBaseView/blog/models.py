from django.db import models

# Create your models here.
class postModel(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField(max_length=500)
    publish_date=models.DateTimeField()
