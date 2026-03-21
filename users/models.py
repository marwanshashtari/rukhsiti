from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    phone_number = models.CharField(max_length=20, blank=True, null=True)

    national_id = models.CharField(max_length=20, unique=True)

    date_of_birth = models.DateField(blank=True, null=True)

    LICENSE_STATUS_CHOICES = [
        ("none", "No License"),
        ("valid", "Valid License"),
        ("suspended", "Suspended"),
        ("expired", "Expired"),
    ]

    license_status = models.CharField(
        max_length=20,
        choices=LICENSE_STATUS_CHOICES,
        default="none"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='instructor_profile')
    experience_years = models.PositiveIntegerField()
    car_type = models.CharField(max_length=50)
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    city = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return f"Instructor: {self.user.username}"
