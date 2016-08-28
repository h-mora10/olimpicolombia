from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput


class StudentUserForm(ModelForm):
    username = forms.CharField(
        max_length=100,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label = "Password Confirmation",
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

    def __init__(self, *args, **kwargs):
        super(StudentUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = TextInput(attrs={
            'id': 'username',
            'class': 'form-control',
            'name': 'username',
            'placeholder': 'Username'})
        self.fields['first_name'].widget = TextInput(attrs={
            'id': 'first_name',
            'class': 'form-control',
            'name': 'first_name',
            'placeholder': 'First Name'})
        self.fields['last_name'].widget = TextInput(attrs={
            'id': 'last_name',
            'class': 'form-control',
            'name': 'last_name',
            'placeholder': 'Last Name'})
        self.fields['email'].widget = EmailInput(attrs={
            'id': 'email',
            'class': 'form-control',
            'name': 'email',
            'placeholder': 'Email'})
        self.fields['password'].widget = PasswordInput(attrs={
            'id': 'password',
            'class': 'form-control',
            'name': 'password',
            'placeholder': 'Password'})
        self.fields['password2'].widget = PasswordInput(attrs={
            'id': 'password2',
            'class': 'form-control',
            'name': 'password2',
            'placeholder': 'Password Confirmation'})


    def clean_username(self):
        #verifica si el usuario existe en la base de datos
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username):
            raise forms.ValidationError('El nombre de usuario ya está registrado. Por favor elija otro.')
        return username

    def clean_password2(self):
        #verifica que password y password2 sean iguales
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden. Por favor intente de nuevo.')
        return password2

    def clean_email(self):
        #verifica si el email existe en la base de datos
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email):
            raise forms.ValidationError('El email ingresado ya está registrado. Por favor elija otro.')
        return email

