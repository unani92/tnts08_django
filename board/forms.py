from django.forms import ModelForm, CharField, ChoiceField
from .models import Board
from ckeditor_uploader.widgets import CKEditorUploadingWidget

c = [('공지','공지'),('일반','일반')]
class BoardForm(ModelForm) : 
    name = CharField(label='이름')
    title = CharField(label='제목')
    choice = ChoiceField(choices=c,label='')
    class Meta : 
        model = Board
        fields = ['choice','name','title','content']
