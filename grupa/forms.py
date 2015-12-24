from django import forms
from django.forms import ModelForm

from django.contrib.auth import get_user_model





class NewGroupForm(forms.Form):
    group_name = forms.CharField(label='Nazwa grupy', max_length = 30,
        widget = forms.TextInput(attrs={'placeholder':'Wpisz nazwę grupy'}))


class NewMemberForm(forms.Form):
    new_member_name = forms.CharField(label='', max_length = 40,
        widget = forms.TextInput(attrs={
            'placeholder':'Wpisz nazwę uczestnika',
            'autofocus': 'autofocus'}))


class MemberForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username']
        #widget = forms.HiddenInput()
        widgets = {
                'username': forms.HiddenInput()}




