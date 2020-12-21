from django.forms import ModelForm
from .models import Recipe, Comment


class RecipeForm(ModelForm):

    class Meta:
        model = Recipe
        fields = ['title', 'items', 'body', 'image']


class CommentFrom(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
