from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Instructor


class RegisterSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField()
    last_name = serializers.CharField()

    phone_number = serializers.CharField()
    national_id = serializers.CharField()
    date_of_birth = serializers.DateField()
    license_status = serializers.CharField()

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "phone_number",
            "national_id",
            "date_of_birth",
            "license_status"
        ]

        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):

        phone_number = validated_data.pop("phone_number")
        national_id = validated_data.pop("national_id")
        date_of_birth = validated_data.pop("date_of_birth")
        license_status = validated_data.pop("license_status")

        user = User.objects.create_user(**validated_data)

        UserProfile.objects.create(
            user=user,
            phone_number=phone_number,
            national_id=national_id,
            date_of_birth=date_of_birth,
            license_status=license_status
        )

        return user
    

class UserProfileDetailSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    username = serializers.CharField(source="user.username")
    email = serializers.EmailField(source="user.email")

    class Meta:
        model = UserProfile
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "national_id",
            "date_of_birth",
            "license_status",
            "created_at",
        ]


class InstructorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    phone_number = serializers.CharField(source='user.profile.phone_number', read_only=True)
    national_id = serializers.CharField(source='user.profile.national_id', read_only=True)
    date_of_birth = serializers.DateField(source='user.profile.date_of_birth', read_only=True)
    license_status = serializers.CharField(source='user.profile.license_status', read_only=True)

    class Meta:
        model = Instructor
        fields = [
            'id',
            'user',
            'username',
            'phone_number',
            'national_id',
            'date_of_birth',
            'license_status',
            'experience_years',
            'car_type',
            'price_per_hour',
            'city',
            'is_available',
        ]
        read_only_fields = ['id', 'user', 'username']