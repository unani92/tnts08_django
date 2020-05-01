from django import forms
from .models import Board, Comment, Reply
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
    hashtag = forms.CharField(
        label=('해시태그'),
        required=False
    )
    class Meta : 
        model = Board
        fields = ['choice','title','content','hashtag']

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

class ReplyForm(forms.ModelForm) :
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
        model = Reply
        fields = ['content']

