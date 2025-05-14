from django.urls import path
from . import views

app_name = 'gym'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Meal Plan URLs
    path('meal-plans/', views.meal_plan_list, name='meal_plan_list'),
    path('meal-plans/<uuid:pk>/', views.meal_plan_detail, name='meal_plan_detail'),
    
    # Workout URLs
    path('workouts/', views.workout_list, name='workout_list'),
    path('workouts/<uuid:pk>/', views.workout_detail, name='workout_detail'),
    
    # Profile URL
    path('profile/', views.profile, name='profile'),
]
