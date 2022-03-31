from crispy_forms.helper import FormHelper
from django import forms
from crispy_forms.layout import Submit, Layout, Row, Column
from company_app.views import Company
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from vacancy_app.views import Vacancy
from .models import Resume


class AddResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'surname', 'status', 'salary', 'specialty', 'grade', 'education', 'experience', 'portfolio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Имя'
        self.fields['surname'].label = 'Фамилия'
        self.fields['status'].label = 'Готовность к работе'
        self.fields['salary'].label = 'Ожидаемое вознаграждение'
        self.fields['specialty'].label = 'Специализвация'
        self.fields['specialty'].empty_label = 'Выберите специализацию'
        self.fields['grade'].label = 'Квалификация'
        self.fields['education'].label = 'Образование'
        self.fields['experience'].label = 'Опыт работы'
        self.fields['portfolio'].label = 'Ссылка на портфолио'
        self.fields['portfolio'].widget.attrs = {'placeholder': 'http://anylink.github.io'}
        self.fields['education'].widget.attrs = {'rows': 4}
        self.fields['experience'].widget.attrs = {'rows': 4}

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('surname', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('status', css_class='form-group col-md-6 mb-0'),
                Column('salary', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('specialty', css_class='form-group col-md-6 mb-0'),
                Column('grade', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('education', css_class='form-group col-md-12'),
            ),
            Row(
                Column('experience', css_class='form-group col-md-12'),
            ),
            Row(
                Column('portfolio', css_class='form-group col-md-12'),
            ),
            Submit('submit', 'Сохранить', css_class='col-8 col-lg-4 offset-2 offset-lg-4')
        )


class UpdateVacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'specialty', 'salary_from', 'salary_to', 'skills', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Название вакансии'
        self.fields['specialty'].label = 'Специализация'
        self.fields['salary_from'].label = 'Зарплата от'
        self.fields['salary_to'].label = 'Зарплата до'
        self.fields['skills'].label = 'Требуемые навыки'
        self.fields['description'].label = 'Описание вакансии'
        self.fields['skills'].widget.attrs = {'rows': 4}
        self.fields['description'].widget.attrs = {'rows': 4}

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6 mb-0'),
                Column('specialty', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('salary_from', css_class='form-group col-md-6 mb-0'),
                Column('salary_to', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('skills', css_class='form-group col-md-12'),
            ),
            Row(
                Column('description', css_class='form-group col-md-12'),
            ),
            Submit('submit', 'Сохранить', css_class='col-8 col-lg-4 offset-2 offset-lg-4')
        )


class AddVacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'specialty', 'salary_from', 'salary_to', 'skills', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Название вакансии'
        self.fields['specialty'].label = 'Специализация'
        self.fields['specialty'].empty_label = 'Выберите категорию'
        self.fields['salary_from'].label = 'Зарплата от'
        self.fields['salary_to'].label = 'Зарплата до'
        self.fields['skills'].label = 'Требуемые навыки'
        self.fields['description'].label = 'Описание вакансии'
        self.fields['skills'].widget.attrs = {'rows': 4}
        self.fields['description'].widget.attrs = {'rows': 4}

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6 mb-0'),
                Column('specialty', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('salary_from', css_class='form-group col-md-6 mb-0'),
                Column('salary_to', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('skills', css_class='form-group col-md-12'),
            ),
            Row(
                Column('description', css_class='form-group col-md-12'),
            ),
            Submit('submit', 'Сохранить', css_class='col-8 col-lg-4 offset-2 offset-lg-4')
        )


class UpdateCompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['name', 'logo', 'employee_count', 'location', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Название компании'
        self.fields['logo'].label = 'Логотип'
        self.fields['employee_count'].label = 'Кол-во человек в компании'
        self.fields['location'].label = 'География'
        self.fields['description'].label = 'Информация о компании'
        self.fields['description'].widget.attrs = {'rows': 4}

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('logo', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('employee_count', css_class='form-group col-md-6 mb-0'),
                Column('location', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('description', css_class='form-group col-md-12'),
            ),
            Submit('submit', 'Изменить', css_class='col-8 col-lg-4 offset-2 offset-lg-4')
        )


class AddCompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['name', 'logo', 'employee_count', 'location', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Название компании'
        self.fields['logo'].label = 'Логотип'
        self.fields['employee_count'].label = 'Кол-во человек в компании'
        self.fields['location'].label = 'География'
        self.fields['description'].label = 'Информация о компании'

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('logo', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('employee_count', css_class='form-group col-md-6 mb-0'),
                Column('location', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                 Column('description', css_class='form-group col-md-12'),
            ),
            Submit('submit', 'Сохранить', css_class='col-8 col-lg-4 offset-2 offset-lg-4')
        )


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
