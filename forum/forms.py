from django import forms

class DodajPorade(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)