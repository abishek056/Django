from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    #https://blog.ctrlbits.com/post/software-development-life-cycle-for-2026

    slug = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    created_by = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return self.title


    
