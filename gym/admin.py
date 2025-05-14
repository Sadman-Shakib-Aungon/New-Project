from django.contrib import admin
from .models import MealPlan, Meal, Workout, Exercise, UserProfile

# Register your models here.
@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'meal_plan', 'calories', 'protein', 'carbs', 'fat', 'time_of_day')
    search_fields = ('name', 'description')
    list_filter = ('time_of_day', 'created_at')

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'duration', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'workout', 'sets', 'reps', 'weight', 'rest_time')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'height', 'weight', 'age', 'fitness_goal')
    search_fields = ('user__username', 'user__email')
    list_filter = ('fitness_goal',)
