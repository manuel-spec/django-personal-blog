from email.policy import default
from django.db import models
from django.urls import reverse
import datetime

class Post(models.Model):
    now = datetime.datetime.now()
    Title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        success_url = 'blogs'
        return reverse('blogs')
        