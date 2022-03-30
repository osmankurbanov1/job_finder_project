from crispy_forms.layout import Submit, Layout, Row, Column
from crispy_forms.helper import FormHelper
from django import forms
from .models import Application


class AddApplication(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['written_username', 'written_phone', 'written_cover_letter']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['written_username'].label = 'Вас зовут'
        self.fields['written_phone'].label = 'Ваш телефон'
        self.fields['written_cover_letter'].label = 'Сопроводительное письмо'

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(

            Row(
                Column('written_username', css_class='form-group col-md-12 mb-0'),
                Column('written_phone', css_class='form-group col-md-12 mb-0'),
                Column('written_cover_letter', css_class='form-group col-md-12 mb-0'),
            ),

            Submit('submit', 'Откликнуться', css_class='col-8 col-lg-4 offset-2 offset-lg-4')
        )
