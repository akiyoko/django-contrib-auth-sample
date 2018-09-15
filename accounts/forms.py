from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2')
