from .models import ShopUser
from django import forms


class RegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               label='پسورد')
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                label='تکرار پسورد')

    class Meta:
        model = ShopUser
        fields = ['first_name', 'last_name', 'phone']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'phone': 'شماره تماس',

        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise forms.ValidationError('شماره تلفن باید عددی باشد')

        if len(phone) != 11:
            raise forms.ValidationError('شماره تلفن باید 11 رقمی باشد')

        if not phone.startswith('09'):
            raise forms.ValidationError('شماره تلفن با 09 آغاز شود')
        return phone

    def clean_password2(self):

        cd = self.cleaned_data
        if len(cd['password']) <= 7:
            raise forms.ValidationError('password too weak!!\nless than 8 character')
        if cd['password'] == '12345678':
            raise forms.ValidationError('too common use another password')
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('no match password!!!')
        return self['password2']


class LoginForm(forms.Form):
    phone = forms.CharField(max_length=11)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               label='پسورد')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise forms.ValidationError('شماره تلفن باید عددی باشد')

        if len(phone) != 11:
            raise forms.ValidationError('شماره تلفن باید 11 رقمی باشد')

        if not phone.startswith('09'):
            raise forms.ValidationError('شماره تلفن با 09 آغاز شود')
        return phone


class SearchForm(forms.Form):
    query = forms.CharField()
