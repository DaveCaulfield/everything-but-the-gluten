from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import CommentForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Recipe
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm



class RecipeList(generic.ListView):
    """
    View for the list of all published recipes
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')  
    template_name = 'index.html'
    paginate_by = 3


class RecipeDetail(View):
    """
    View recipe details
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )       


class RecipeLike(View):

    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))



class RecipeCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Recipe
    fields = ['title', 'featured_image', 'preparation_time', 'cooking_time', 'ingredients', 'instructions']
    template_name = 'recipe_form.html'
    success_url = reverse_lazy('my_pending_recipes')
    success_message = "Thank You! Your recipe is awaiting approval by our team"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, generic.UpdateView):
    model = Recipe
    fields = ['title', 'featured_image', 'preparation_time', 'cooking_time', 'ingredients', 'instructions']
    template_name = 'recipe_form.html'
    success_url = reverse_lazy('my_pending_recipes')
    success_message = "Your recipe update will be reviewd"

    def form_valid(self, form):
        if self.object.status == 1:
            form.instance.status = 0
        return super().form_valid(form)
       
    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False



class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Recipe
    template_name = 'recipe_confirm_delete.html'
    success_url = reverse_lazy('my_published_recipes')
    success_message = "Your recipe has been deleted"

     
    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False


class PublishedList(generic.ListView):

    model = Recipe  
    template_name = 'my_published_recipes.html'
    paginate_by = 3

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user, status=1).order_by('-created_on')



class PendingList(generic.ListView):

    model = Recipe  
    template_name = 'my_pending_recipes.html'
    paginate_by = 3
    
    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user, status=0).order_by('-created_on')



class FavouriteList(generic.ListView):

    model = Recipe  
    template_name = 'my_favourite_recipes.html'
    paginate_by = 3

    def get_queryset(self):
        user = self.request.user
        queryset = Recipe.objects.filter(likes=user.id)
        return queryset



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })



    