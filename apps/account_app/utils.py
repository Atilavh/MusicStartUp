import random
from .models import OTP


# region GenerateOtp
def generate_otp(user):
    user.otps.filter(is_verified=False).update(is_verified=True)
    code = str(random.randint(100000, 999999))
    otp = OTP.objects.create(user=user, code=code)

    # TODO: Send SMS....
    print(f"OTP for {user.phone}: {code}")
    return otp

# endregion

# region VerifyOtp
def verify_otp(user, code):
    otp = user.latest_otp
    if not otp or otp.code != code:
        return False

    otp.is_verified = True
    otp.save()

    user.is_active = True
    user.save()
    return True
# endregion