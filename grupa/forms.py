from django import forms




class NewGroupForm(forms.Form):
    group_name = forms.CharField(label='Nazwa grupy', max_length = 30,
        widget = forms.TextInput(attrs={'placeholder':'Wpisz nazwę grupy'}))


class NewMemberForm(forms.Form):
    new_member_name = forms.CharField(label='Nazwa uczestnika', max_length = 40,
        widget = forms.TextInput(attrs={'placeholder':'Wpisz nazwę uczestnika, którego chcesz dodać do grupy'}))
