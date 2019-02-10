from django.db import models
from django.utils import timezone



class ContactEmail(models.Model):
    name = models.CharField(max_length=200)
    subject=models.CharField(max_length=400)
    message=models.TextField()
    email=models.EmailField(max_length=254)
    
class AlgorithmCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class AlgorithmPost(models.Model):
    category = models.ForeignKey(AlgorithmCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to="algopost/%Y/%m/%d", blank=True, null=True)
    shortDescription = models.TextField(max_length=400)
    description = models.TextField(blank=True)
    dateTime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to="post/%Y/%m/%d", blank=True, null=True)
    shortDescription = models.TextField(max_length=400)
    description = models.TextField(blank=True)
    dateTime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
