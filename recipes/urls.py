from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('add/', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('<slug:slug>/update/', views.RecipeUpdateView.as_view(), name='recipe_update'),
    path('<slug:slug>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
   
    
    
]