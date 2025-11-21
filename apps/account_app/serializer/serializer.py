import re
from rest_framework import serializers
from apps.account_app.models import User


# region UserRegisterSerializer
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone']

    def validate_phone(self, value):
        pattern = r'^09\d{9}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("phoen number is not valid")
        return value
# endregion

# region OTPVerifySerializer
class OTPVerifySerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11)
    otp = serializers.CharField(max_length=6)

    def validate_phone(self, value):
        pattern = r'^09\d{9}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("Phone must be 11 digits and start with 09")
        return value

    def validate_otp(self, value):
        pattern = r'^\d{6}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("OTP must be 6 digits")
        return value
# endregion