from django.urls import path
from .views import register_user, current_user_profile, InstructorListCreateView, InstructorDetailView

urlpatterns = [
    path("register/", register_user, name="register"),
    path("me/", current_user_profile, name="current_user_profile"),
    path('instructors/', InstructorListCreateView.as_view(), name='instructor-list-create'),
    path('instructors/<int:pk>/', InstructorDetailView.as_view(), name='instructor-detail'),
]