from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# each class will be its own table in a db
# each attribute will be a different field in a db
# LEARN:
# working with & importing modules
# working with & importing classes and functions within those modules

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
