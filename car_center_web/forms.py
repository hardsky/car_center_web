from django import forms

class CarForm(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField()
