from . import views
from django.urls import path

urlpatterns = [

    path('<slug:slug>/update/', views.RecipeUpdateView.as_view(),
         name='recipe_update'),
    path('admin_area/', views.AdminPendingList.as_view(),
         name='admin_area'),
    path('<slug:slug>/admin_update/', views.AdminRecipeUpdateView.as_view(),
         name='admin_recipe_update'),
    path('change_password/', views.change_password,
         name='change_password'),
    path('my_published_recipes/', views.PublishedList.as_view(),
         name='my_published_recipes'),
    path('my_pending_recipes/', views.PendingList.as_view(),
         name='my_pending_recipes'),
    path('my_favourite_recipes/', views.FavouriteList.as_view(),
         name='my_favourite_recipes'),
    path('', views.home, name='home'),
    path('recipe_page_list/', views.RecipeList.as_view(),
         name='recipe_page_list'),
    path('add/', views.RecipeCreateView.as_view(),
         name='recipe_create'),
    path('<slug:slug>/', views.RecipeDetail.as_view(),
         name='recipe_detail'),
    path('<slug:slug>/delete/', views.RecipeDeleteView.as_view(),
         name='recipe_delete'),
    path('like/<slug:slug>', views.RecipeLike.as_view(),
         name='recipe_like'),
]
