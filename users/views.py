from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status,generics
from .serializers import RegisterSerializer, UserProfileDetailSerializer, InstructorSerializer
from rest_framework.permissions import IsAuthenticated 
from .models import Instructor


@api_view(["POST"])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def current_user_profile(request):
    serializer = UserProfileDetailSerializer(request.user.profile)
    return Response(serializer.data)


class InstructorListCreateView(generics.ListCreateAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return []

    def get_queryset(self):
        queryset = Instructor.objects.all()

        city = self.request.query_params.get('city')
        price_min = self.request.query_params.get('price_min')
        price_max = self.request.query_params.get('price_max')
        is_available = self.request.query_params.get('is_available')

        if city:
            queryset = queryset.filter(city__iexact=city)

        if price_min:
            queryset = queryset.filter(price_per_hour__gte=price_min)

        if price_max:
            queryset = queryset.filter(price_per_hour__lte=price_max)

        if is_available is not None:
            if is_available.lower() == 'true':
                queryset = queryset.filter(is_available=True)
            elif is_available.lower() == 'false':
                queryset = queryset.filter(is_available=False)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class InstructorDetailView(generics.RetrieveAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer