from django.db import models


# Create your models here.

class Project(models.Model):
    project_title = models.CharField(max_length=20)
    project_description = models.TextField(max_length=20)
    project_url = models.URLField(blank=True)

    def __str__(self):
        return self.project_title
