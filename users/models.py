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
