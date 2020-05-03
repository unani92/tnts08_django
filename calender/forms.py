from django import forms
from .models import JoinMatch, Join, Dismiss
from tempus_dominus.widgets import DatePicker, TimePicker

choice1 = [('home','home'),('away','away')]
choice2 = [('League','League'),('ACL','ACL'),('FA','FA')]

class JoinMatchForm(forms.ModelForm):
    home_away = forms.ChoiceField(
        choices=choice1,
        label='홈/원정'
    )
    league_acl_fa = forms.ChoiceField(
        choices=choice2,
        label='경기 종류'
    )
    date = forms.DateTimeField(
        widget= DatePicker(
            options={
                'minDate': '2020-01-01',
            }
        ),
        initial='2013-01-01',
    )
    highlight = forms.BooleanField(required=False)

    class Meta:
        model = JoinMatch
        fields = ['home_away','league_acl_fa','vs','highlight','date']

class JoinForm(forms.ModelForm):
    time = forms.TimeField(
        widget=TimePicker(
            options={
                'enabledHours': list(range(0,24)),
                'defaultDate': '1970-01-01T14:56:00'
            },
            attrs={
                'input_toggle': True,
                'input_group': True,
            },
        ),
    )
    class Meta:
        model = Join
        fields = ['time']