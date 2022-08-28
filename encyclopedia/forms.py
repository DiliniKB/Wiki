from django import forms

class newEntry(forms.Form):
    title = forms.CharField(label="Enter title")
    description = forms.CharField(label="Enter description")