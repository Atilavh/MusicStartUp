from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from apps.account_app.models import User
from .permissions import IsSuperUser
from .serializer.serializer import UserListSerializer, UserPermissionSerializer


# region UserListView
@api_view(['GET'])
@permission_classes([IsSuperUser])
def user_list_view(request):
    users = User.objects.all()
    serializer = UserListSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
# endregion


# region UserPermissionView
@api_view(['GET', 'PATCH'])
@permission_classes([IsAdminUser])
def user_permission_view(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    permission = user.user_permission

    if request.method == 'GET':
        serializer = UserPermissionSerializer(permission)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PATCH':
        serializer = UserPermissionSerializer(permission, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# endregion