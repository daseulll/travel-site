from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email

class SignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].validator = [validate_email]
        self.fields['username'].help_text = '이메일형식으로 입력해주세요.'
        self.fields['username'].label = 'E-mail'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].help_text = '비밀번호는 8자 이상이여야 하며,\n숫자만 사용할 수 없습니다.'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = user.username
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

