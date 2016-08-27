from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class StudentUserForm(ModelForm):
    username = forms.CharField(
        max_length=100,
    )
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput()
    )
    email = forms.EmailField(
        max_length=200,
    )
    first_name = forms.CharField(
        max_length=100,
    )
    last_name = forms.CharField(
        max_length=100,
    )

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email', 'first_name', 'last_name']

    def clean_username(self):
        #verifica si el usuario existe en la base de datos
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('El nombre de usuario ya está registrado. Por favor elija otro.')
        return username

    def clean_email(self):
        #verifica si el email existe en la base de datos
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('El email ingresado ya está registrado. Por favor elija otro.')
        return email

    def clean_password(self):
        #verifica que password y password2 sean iguales
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden. Por favor intente de nuevo.')
        return password2