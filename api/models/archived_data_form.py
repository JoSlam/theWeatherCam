from django import forms

class Archived_data_form(forms.Form):
    date = forms.DateField(widget=forms.TextInput(attrs={"type":"date", 'class':'form-control'}))