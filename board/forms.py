from django.forms import ModelForm, CharField, TextInput
from .models import Board
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class BoardForm(ModelForm) : 
    class Meta : 
        model = Board
        fields = ['title','content']

        widget = {
            # 'title' : TextInput(
            #     attrs={
            #         'class' : 'form-control',
            #         'style' : 'width:100%',
            #         'placeholder' : 'press title',
            #     }
            # ),
            'content' : CharField(widget=CKEditorUploadingWidget(), label='')
        }