from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MealPlan, Meal, Workout, Exercise, UserProfile
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    """Home page view"""
    return render(request, 'gym/home.html')

@login_required
def dashboard(request):
    """User dashboard view"""
    user_meal_plans = MealPlan.objects.filter(user=request.user).order_by('-created_at')
    user_workouts = Workout.objects.filter(user=request.user).order_by('-created_at')

    context = {
        'meal_plans': user_meal_plans,
        'workouts': user_workouts,
    }

    return render(request, 'gym/dashboard.html', context)

# Meal Plan Views
@login_required
def meal_plan_list(request):
    """View all meal plans for the logged-in user"""
    meal_plans = MealPlan.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'gym/meal_plans/list.html', {'meal_plans': meal_plans})

@login_required
def meal_plan_detail(request, pk):
    """View a specific meal plan and its meals"""
    meal_plan = get_object_or_404(MealPlan, pk=pk, user=request.user)
    meals = meal_plan.meals.all().order_by('time_of_day')
    return render(request, 'gym/meal_plans/detail.html', {'meal_plan': meal_plan, 'meals': meals})

# Workout Views
@login_required
def workout_list(request):
    """View all workouts for the logged-in user"""
    workouts = Workout.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'gym/workouts/list.html', {'workouts': workouts})

@login_required
def workout_detail(request, pk):
    """View a specific workout and its exercises"""
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    exercises = workout.exercises.all()
    return render(request, 'gym/workouts/detail.html', {'workout': workout, 'exercises': exercises})

# User Profile Views
@login_required
def profile(request):
    """View and edit user profile"""
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)

    return render(request, 'gym/profile.html', {'profile': profile})
