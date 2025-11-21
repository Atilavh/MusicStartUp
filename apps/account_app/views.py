from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializer.serializer import *
from .utils import generate_otp, verify_otp



# region RegisterView
@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        validated_data = serializer.validated_data
        phone = validated_data['phone']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        user, created = User.objects.get_or_create(
            phone=phone,
            defaults={
                'first_name': first_name,
                'last_name': last_name,
                'is_active': False
            }
        )
        otp = generate_otp(user)
        return Response({"message": "OTP sent to your phone."}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# endregion

# region VerifyView
@api_view(['POST'])
@permission_classes([AllowAny])
def verify_view(request):
    serializer = OTPVerifySerializer(data=request.data)
    if serializer.is_valid():
        validated_data = serializer.validated_data
        phone = validated_data['phone']
        otp_code = validated_data['otp']

        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        if verify_otp(user, otp_code):
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            })

        return Response({"error": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# endregion

# region LoginView
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    serializer = OTPVerifySerializer(data=request.data)
    if serializer.is_valid():
        validated_data = serializer.validated_data
        phone = validated_data['phone']
        otp_code = validated_data['otp']

        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        if verify_otp(user, otp_code):
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            })

        return Response({"error": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# endregion

# region LogoutView
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
# endregion
