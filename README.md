# Gym Fitness Tracker

A Django-based web application for tracking workouts, planning meals, and achieving fitness goals.

## Features

- User authentication and profile management
- Meal planning with nutritional information
- Workout tracking with exercise details
- Responsive design using Bootstrap

## Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Create a superuser: `python manage.py createsuperuser`
5. Run the development server: `python manage.py runserver`

## Models

- MealPlan: For creating and managing meal plans
- Meal: For individual meals within a meal plan
- Workout: For creating and managing workout routines
- Exercise: For individual exercises within a workout
- UserProfile: For storing user fitness information

## License

This project is licensed under the MIT License - see the LICENSE file for details.
