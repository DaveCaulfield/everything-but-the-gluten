from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin, SummernoteWidget
from .models import Recipe, Comment


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Backend administration recipe area
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('ingredients', 'instructions')
    actions = ['approve_recipe']

    def approve_recipe(self, request, queryset):
        """
        approve recipe
        """
        queryset.update(approved=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    backend administration comment area
    """
    list_display = ('name', 'body', 'recipe', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        approve comments
        """
        queryset.update(approved=True)
