from django.contrib.auth.backends import ModelBackend
from .models import RetailUser
from django.contrib.auth import get_user_model

class RetailUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

"""
class LocalUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = LocalUser.objects.get(username=username)
            if user.check_password(password):
                return user
        except LocalUser.DoesNotExist:
            return None
"""

