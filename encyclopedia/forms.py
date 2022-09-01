from pydoc import describe
# from turtle import title
from django import forms
from . import util

class newEntry(forms.Form):
    
    title = forms.CharField(
        max_length=100,
        required=True
    )

    description = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def clean_title(self):
        """Validate if title exists."""

        title = self.cleaned_data.get('title')
        if title in util.list_entries():
            raise forms.ValidationError('Name exists. Take another.')

        return title


def editEntry(newEntry):

    def clean_title(self):
        title = self.cleaned_data.get('title')
        return title
    
    def update_entry_file(self, title, description):
        with open(f'./entries/{title}.md', 'w') as ef:
            ef.write(f'# {title}\n' + description)