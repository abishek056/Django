from django.db import models
from django.utils.text import slugify

# create your models here
class Category(models.Model):
    name = models.CharField(max_length=54)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blog_images/', default='blog_images/default.jpg')

    slug = models.CharField(max_length=200, unique=True, blank=True)
    author = models.CharField(max_length=100)
    # category = models.CharField(max_length=100)
    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # base_slug = self.title.lower().replace(' ', '-')
            base_slug = slugify (self.title)
            slug = base_slug
            counter = 1

            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


