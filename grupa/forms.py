from django import forms
from django.forms import ModelForm

from django.contrib.auth import get_user_model

from .models import CustomGroup



class NewGroupForm(forms.Form):
    group_name = forms.CharField(label='Nazwa grupy  ', max_length = 30,
        widget = forms.TextInput(attrs={'placeholder':'Wpisz nazwę grupy'}))
    #stacje = forms.BooleanField(label='Czy grupa ma dostawać raporty o stacjach?  ', required = False)
    #magazyny = forms.BooleanField(label='Czy grupa ma dostawać raporty o magazynach?  ', required = False)


class DeleteGroupForm(ModelForm):
    class Meta:
        model = CustomGroup
        fields = ['group_creator']
        widgets = {
                'group_creator': forms.HiddenInput()}


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




