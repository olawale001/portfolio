from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    image = models.FileField(upload_to="project_images/", blank=True)
    
   
