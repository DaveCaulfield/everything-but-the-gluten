from .models import Comment, Recipe
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class recipeForm(forms.Form):
    title = forms.CharField(label='name', max_length=100)


