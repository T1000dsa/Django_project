from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()
        print(__name__)
        try:
            user = user_model.objects.get(email=username)

            if user.check_password(password):
                return user
            else:
                return None 
                
        except (user_model.DoesNotExist, user_model.MultipleObjectsReturned):
            return None
    def get_user(self, user_id):
        user_model = get_user_model() 
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None