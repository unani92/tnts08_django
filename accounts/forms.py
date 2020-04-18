from django import forms
from .models import MyUser
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm, UserChangeForm

class MyUserCreationForm(UserCreationForm) : 
    username = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'ID를 입력하세요'
                }
            )
        )
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
    address = forms.CharField(
        label=("주소"),
        widget=forms.TextInput(attrs={'placeholder': '주소를 입력하시오'}),
        strip=False,
        help_text=(''),
    )
    class Meta:
        model = MyUser
        fields = ('first_name','email','address','username')
        field_classes = {'username': UsernameField}

class MyAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label=('ID'),
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'placeholder':'아이디'
            }
        )
    )

class MyUserChangeForm(UserChangeForm):
    address = forms.CharField(
        label=("주소"),
        widget=forms.TextInput(
            attrs={
                'placeholder': '주소를 입력하시오',

            }
        ),
        strip=False,
        help_text=(''),
    )
    class Meta:
        model = MyUser
        fields = ['username', 'first_name','address', 'email']