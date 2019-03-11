from django import forms
from .models import Post, Comment
# from django.contrib.auth.forms import UserCreationForm

# class SignupForm(UserCreationForm):
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].validator = [validator_email]
#         self.fields['username'].help_text = '이메일형식으로 입력해주세요.'
#         self.fields['username'].label = 'E-mail'
    
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.email = user.username
#         if commit:
#             user.save()
#         return user


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'text',
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)
