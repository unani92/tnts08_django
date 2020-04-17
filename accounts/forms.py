from django import forms
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm) : 
    password1 = forms.CharField(
        label=("비밀번호"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'placeholder' : '비밀번호'
                }
            ),
        help_text='비밀번호는 8자 이상 작성해주세요',
    )
    password2 = forms.CharField(
        label=("비밀번호 확인"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=(''),
    )