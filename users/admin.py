from django.contrib import admin
from .models import Instructor, UserProfile

admin.site.register(UserProfile)
admin.site.register(Instructor)