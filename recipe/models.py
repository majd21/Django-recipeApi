from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    items = models.TextField()
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='recipe/images/')
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    recipe = models.ForeignKey(Recipe , on_delete=models.CASCADE , related_name='comments')

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.recipe) 
