import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gymproject.settings')
django.setup()

from django.contrib.auth.models import User
from django.db import IntegrityError

# Try to create a new superuser with a very simple password
try:
    # First, check if the user already exists
    if User.objects.filter(username='simple').exists():
        # If it exists, update the password
        user = User.objects.get(username='simple')
        user.set_password('simple123')
        user.save()
        print("Updated password for existing user 'simple' to 'simple123'")
    else:
        # Create a new user
        User.objects.create_superuser(
            username='simple',
            email='simple@example.com',
            password='simple123',
            is_staff=True,
            is_active=True,
            is_superuser=True
        )
        print("Created new superuser 'simple' with password 'simple123'")
except IntegrityError:
    print("User already exists, updating password...")
    user = User.objects.get(username='simple')
    user.set_password('simple123')
    user.save()
    print("Updated password for user 'simple' to 'simple123'")
except Exception as e:
    print(f"Error: {e}")
