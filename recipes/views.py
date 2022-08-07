from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import CommentForm, RecipeForm
from .forms import RecipeUpdateForm, AdminRecipeUpdateForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Recipe, Comment
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


class RecipeList(generic.ListView):
    """
    display list of all published recipes
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipe_page_list.html'
    paginate_by = 6


def home(request):
    return render(request, 'index.html')


class RecipeDetail(View):
    """
    display recipe details page
    """

    def get(self, request, slug, *args, **kwargs):
        """
        get the recipe, check for comments and likes
        """
        queryset = Recipe.objects
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
        """
        get the recipe, check for comments and likes.
        If a comment post request is valid  then save.
        """
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
    """
    Recipe like feature
    """

    def post(self, request, slug, *args, **kwargs):
        """
        toggle likes on/off. two options.
        if user has liked recipe then remove like.
        if user has not liked recipe the add like.
        """
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class RecipeCreateView(
                       LoginRequiredMixin,
                       SuccessMessageMixin,
                       generic.CreateView):
    """
    Create a recipe
    """                  
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_form.html'
    success_url = reverse_lazy('my_pending_recipes')
    success_message = "Thank You! Your recipe is awaiting approval by our team"

    def form_valid(self, form):
        """
        assign the user thats signed in as the author
        """
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(
                       LoginRequiredMixin,
                       UserPassesTestMixin,
                       SuccessMessageMixin,
                       generic.UpdateView):
    """
    Update a recipe
    """
    model = Recipe
    form_class = RecipeUpdateForm
    template_name = 'recipe_update_form.html'
    success_url = reverse_lazy('my_published_recipes')
    success_message = "Thank You! your update is awaiting approval by our team"

    def form_valid(self, form):
        """
        change the recipe status from published to draft then save.
        allows for admin approval.
        """ 
        if self.object.status == 1:
            form.instance.status = 0
        return super().form_valid(form)

    def test_func(self):
        """
        rule that only author of recipe can update recipe
        """
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False


class RecipeDeleteView(
                       LoginRequiredMixin,
                       UserPassesTestMixin,
                       generic.DeleteView):
    """
    Delete a recipe
    """
    model = Recipe
    template_name = 'recipe_confirm_delete.html'
    success_url = reverse_lazy('my_published_recipes')
    success_message = "Your recipe has been deleted"

    def test_func(self):
        """
        rule that only author of recipe can delete recipe
        """
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False

    def delete(self, request, *args, **kwargs):
        """
        display success message for delete recipe.
        """
        messages.success(self.request, self.success_message)
        return super(RecipeDeleteView, self).delete(request, *args, **kwargs)


class PublishedList(generic.ListView):
    """
    Display users published recipes
    """
    model = Recipe
    template_name = 'my_published_recipes.html'
    paginate_by = 3

    def get_queryset(self):
        """
        get recipes where author is the signed in user and status is published.
        """
        return Recipe.objects.filter(
                                     author=self.request.user,
                                     status=1).order_by('-created_on')


class PendingList(generic.ListView):
    """
    Display users pending recipes
    """
    model = Recipe
    template_name = 'my_pending_recipes.html'
    paginate_by = 3

    def get_queryset(self):
        """
        get recipes where author is the signed in user and status is pending.
        """
        return Recipe.objects.filter(
                                     author=self.request.user,
                                     status=0).order_by('-created_on')


class FavouriteList(generic.ListView):
    """
    Display users favourite recipes
    """
    model = Recipe
    template_name = 'my_favourite_recipes.html'
    paginate_by = 3

    def get_queryset(self):
        """
        get recipes marked as liked by the signed in user.
        """
        user = self.request.user
        queryset = Recipe.objects.filter(likes=user.id)
        return queryset



def change_password(request):
    """
    Change password form.
    """
    # change password code is from simpleisbetterthancomplex.com
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(
                             request,
                             'Your password was successfully updated!')

            return redirect('change_password')

        else:
            messages.error(request, 'Please correct the error below.')

    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })


class AdminPendingList(generic.ListView):
    """
    Display recipes waiting for admin approval.
    """
    model = Recipe
    template_name = 'admin_area.html'
    paginate_by = 3

    def get_queryset(self):
        """
        get recipes in draft status.
        """
        return Recipe.objects.filter(status=0).order_by('-created_on')


class AdminRecipeUpdateView(
                            LoginRequiredMixin,
                            SuccessMessageMixin,
                            generic.UpdateView):
    """
    Admins recipe update view. allows admin front end approval 
    """
    model = Recipe
    form_class = AdminRecipeUpdateForm
    template_name = 'admin_recipe_form.html'
    success_url = reverse_lazy('admin_area')
    success_message = "Recipe updated"

    def form_valid(self, form):
        """
        save updated form
        """
        return super().form_valid(form)
