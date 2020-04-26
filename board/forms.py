from django import forms
from .models import Board, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget

c = [('일반','일반'),('공지','공지')]
class BoardForm(forms.ModelForm) : 

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
        fields = ['choice','title','content']

class CommentForm(forms.ModelForm) :
    content = forms.CharField(
        label=(''),
        widget=forms.Textarea(
            attrs={
                'placeholder': '댓글은 200자까지 작성 가능합니다.',
                'style' : 'height:100px;'
            }
        )
    )
    class Meta:
        model = Comment
        fields = ['content']
