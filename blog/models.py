from django.db import models


# Create your models here.

class Blog(models.Model):
    post_title = models.CharField(max_length=100)
    post_description = models.TextField(max_length=500)
    post_photo = models.ImageField(upload_to='blog/media')
    post_url = models.URLField(blank=True)
    post_date = models.DateField()

    def __str__(self):
        return self.post_title
