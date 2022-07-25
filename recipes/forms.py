from .models import Comment, Recipe
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class AdminAreaForm(forms.Form):
    title = forms.CharField()


