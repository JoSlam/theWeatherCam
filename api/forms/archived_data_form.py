from django import forms

class ArchivedDataForm(forms.Form):
    date = forms.DateField(widget=forms.TextInput(attrs={"type":"date", 'class':'form-control'}))