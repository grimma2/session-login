from django import forms
from django.core.exceptions import ValidationError


class PhoneForm(forms.Form):
    phone = forms.CharField(label='Введите телефон в формате +7...', max_length=14)

    def clean_phone(self):
        data = self.cleaned_data['phone']
        
        if not data.startswith('+7'):
            raise ValidationError('Телефон должен начинаться на +7')
        
        for digit in data:
            try:
                int(digit)
            except ValueError:
                raise ValidationError('Телефон содержит недопустимые символы')

        return data


class CodeForm(forms.Form):
    code = forms.CharField(label='Введите код из телеграмма', max_length=30)
