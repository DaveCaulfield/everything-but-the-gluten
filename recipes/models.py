"""Imports"""
from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import RegexValidator


STATUS = ((0, "Draft"), (1, "Published"))
alphanumeric = RegexValidator(r'^\w+( \w+)*$', 'Only alphanumeric characters are allowed.')



class Recipe(models.Model):
    """
    Model for recipe
    """
    title = models.CharField(max_length=200, unique=True, validators=[alphanumeric])
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    preparation_time_minutes = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(900)])
    cooking_time_minutes = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(900)])
    ingredients = models.TextField()
    instructions = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='like_recipe', blank=True)
    approved = models.BooleanField(default=False)
    

    class Meta:
        """
        Orders recipes by date created - newest first
        """
        ordering = ['-created_on']

    def __str__(self):
        """Magic Method, returns a string description of the object"""
        return self.title

    def number_of_likes(self):
        """Helper method, returns the amount of likes on a recipe"""
        return self.likes.count()

    def save(self, *args, **kwargs):
        """ slugify function from learndjango.com"""
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


    


class Comment(models.Model):
    """
    Comments model. Authenticated memebers can comment on a recipe
    """
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Orders recipes by date created - newest first
        """
        ordering = ['created_on']

    def __str__(self):
        """Magic Method, returns a string description of the object"""
        return f"Comment {self.body} by {self.name}"

