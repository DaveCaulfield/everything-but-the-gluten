from .models import Comment, Recipe
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    """
    comments form
    """
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    """
    Recipe form
    """

    class Meta:
        model = Recipe
        fields = (
            'title',
            'featured_image',
            'preparation_time_minutes',
            'cooking_time_minutes',
            'ingredients',
            'instructions',
            )
        widgets = {
            'ingredients': SummernoteWidget(),
            'instructions': SummernoteWidget(),
        }


class RecipeUpdateForm(forms.ModelForm):
    """
    Recipe update form
    """

    class Meta:
        model = Recipe
        fields = (
                  'title',
                  'featured_image',
                  'preparation_time_minutes',
                  'cooking_time_minutes',
                  'ingredients',
                  'instructions',
                  )
        widgets = {
            'ingredients': SummernoteWidget(),
            'instructions': SummernoteWidget()
        }


class AdminRecipeUpdateForm(forms.ModelForm):
    """
    Admins Recipe update form
    """

    class Meta:
        model = Recipe
        fields = (
                  'title',
                  'featured_image',
                  'preparation_time_minutes',
                  'cooking_time_minutes',
                  'ingredients',
                  'instructions',
                  'status',
                  'approved'
            )
        widgets = {
            'ingredients': SummernoteWidget(),
            'instructions': SummernoteWidget()
        }
