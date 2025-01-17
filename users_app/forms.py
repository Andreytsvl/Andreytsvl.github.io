from django import forms
from django.contrib.auth.forms import AuthenticationForm # из коробки
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users_app.models import User


class UserLoginForm(AuthenticationForm):



    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField()
    password = forms.CharField()


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (

            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )


    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()



class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "email",
            "phone_number",)

    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    phone_number=forms.CharField()



