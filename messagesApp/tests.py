from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User


superusers = User.objects.filter(is_superuser=True)

print(superusers)