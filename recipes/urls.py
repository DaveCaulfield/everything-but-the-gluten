from . import views
from .views import AdminAreaFormView
from django.urls import path

urlpatterns = [
    
    path('admin_area/', AdminAreaFormView.as_view(), name='admin_area'),
    path('change_password/', views.change_password, name='change_password'),
    path('my_published_recipes/', views.PublishedList.as_view(), name='my_published_recipes'),
    path('my_pending_recipes/', views.PendingList.as_view(), name='my_pending_recipes'),
    path('my_favourite_recipes/', views.FavouriteList.as_view(), name='my_favourite_recipes'),
    path('', views.RecipeList.as_view(), name='home'),
    path('add/', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('<slug:slug>/update/', views.RecipeUpdateView.as_view(), name='recipe_update'),
    path('<slug:slug>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    
  
   
]