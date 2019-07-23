from django.db import models
from django.conf import settings

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/images/', blank = True)
    # file = models.FileField(null=True)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]