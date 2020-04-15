from django import forms
from .models import Board
from ckeditor_uploader.widgets import CKEditorUploadingWidget

c = [('일반','일반'),('공지','공지')]
class BoardForm(forms.ModelForm) : 
    name = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder':'이름을 입력하시오'
            }
        )
    ) 
    
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder':'제목을 입력하시오'
            }
        ) 
    )
    choice = forms.ChoiceField(choices=c,label='')
    class Meta : 
        model = Board
        fields = ['choice','name','title','content']
