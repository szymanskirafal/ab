from django import forms




class NewGroupForm(forms.Form):
    group_name = forms.CharField(label='Nazwa grupy', max_length = 30,
        widget = forms.TextInput(attrs={'placeholder':'Wpisz nazwę grupy'}))

