from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'required': '',
            'name': 'username',
            'id': 'username',
            'type': 'text',
            'placeholder': 'Joji',
            'class': 'form-control',
            'value': '',
        })
        self.fields['password1'].widget.attrs.update({
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'placeholder': 'Enter Password',
            'class': 'form-control',
        })
        self.fields['password2'].widget.attrs.update({
            'required': '',
            'name': 'password2',
            'id': 'password2',
            'type': 'password',
            'placeholder': 'Re-type Password',
            'class': 'form-control',
        })
        self.fields['email'].widget.attrs.update({
            'required': '',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'placeholder': 'iu@uwu.com',
            'class': 'form-control',
        })

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def clean(self):
        super(RegisterForm, self).clean()
        username = self.cleaned_data.get('username')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 != password2:
            self._errors['password2'] = self.error_class(['Password mismatch'])
        if len(password1) < 8:
            self._errors['password1'] = self.error_class(['Password length must be at least 8 characters'])
        if len(username) < 4:
            self._errors['username'] = self.error_class(['Username must be at least 4 characters'])

        return self.cleaned_data
