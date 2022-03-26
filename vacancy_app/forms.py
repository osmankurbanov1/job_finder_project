from crispy_forms.layout import Submit, Layout, Row, Column
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='col-8 col-lg-4 offset-2 offset-lg-4'),
                Column('password', css_class='col-8 col-lg-4 offset-2 offset-lg-4'),
            ),
            Submit('submit', 'Войти', css_class='col-8 col-lg-4 offset-2 offset-lg-4')
        )

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))

    # class Meta:
    #     model = User
    #     fields = ('username', 'first_name', 'last_name', 'password1')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='col-8 col-lg-4 offset-2 offset-lg-4'),
                Column('first_name', css_class='col-8 col-lg-4 offset-2 offset-lg-4'),
                Column('last_name', css_class='col-8 col-lg-4 offset-2 offset-lg-4'),
                Column('password1', css_class='col-8 col-lg-4 offset-2 offset-lg-4'),
            ),
            Submit('submit', 'Зарегистрироваться', css_class='col-8 col-lg-4 offset-2 offset-lg-4')
        )
