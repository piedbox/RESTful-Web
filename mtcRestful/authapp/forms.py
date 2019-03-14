from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from authapp.models import CustomUsers

from django.contrib.auth.forms import UserChangeForm


class UsersLoginForm(AuthenticationForm):
    """Форма входа пользователя."""
    class Meta:
        model = CustomUsers
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UsersLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UsersRegisterForm(UserCreationForm):
    """Форма регистрации пользователя."""

    class Meta:
        model = CustomUsers
        fields = ('username', 'first_name', 'last_name', 'gender', 'password1', 'password2', 'email')

    def __init__(self, *args, **kwargs):
        super(UsersRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class UsersEditForm(UserChangeForm):
    """Форма изменения данных пользователя."""

    class Meta:
        model = CustomUsers
        fields = ('username', 'first_name', 'last_name', 'gender',
                  'email', 'password')

    def __init__(self, *args, **kwargs):
        super(UsersEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()
