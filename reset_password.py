import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gymproject.settings')
django.setup()

from django.contrib.auth.models import User

# Get the admin user
admin = User.objects.get(username='admin')

# Set a new password
admin.set_password('StrongPassword123')
admin.save()

print("Password for 'admin' has been reset to 'StrongPassword123'")
