from .models import Comment, Recipe
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)




class RecipeForm(forms.ModelForm):
   
    class Meta:
        model = Recipe
        fields = (
            'title', 'featured_image', 'preparation_time', 'cooking_time', 'ingredients', 'instructions',
            )
        widgets = {
            'ingredients': SummernoteWidget(),
            'instructions': SummernoteWidget(),
        }


class RecipeUpdateForm(forms.ModelForm):
   
    class Meta:
        model = Recipe
        fields = (
            'title', 'featured_image', 'preparation_time', 'cooking_time', 'ingredients', 'instructions',
            )
        widgets = {
            'ingredients': SummernoteWidget(),
            'instructions': SummernoteWidget()
        }


class AdminRecipeUpdateForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = (
            'title', 'featured_image', 'preparation_time', 'cooking_time', 'ingredients', 'instructions', 'status', 'approved'
            )
        widgets = {
            'ingredients': SummernoteWidget(),
            'instructions': SummernoteWidget()
        }