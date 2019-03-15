from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from .models import Profile

class SignupForm(UserCreationForm):
    name = forms.CharField(max_length=30)

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

        name = self.cleaned_data.get('name', None)
        Profile.objects.create(user=user, name=name)
        return user

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('name',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'bio']
