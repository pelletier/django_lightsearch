"""
The forms are the human way to interact with the search engine (for now).
"""

from django import forms

class SearchForm(forms.Form):
    """The form used to receive queries"""
    query = forms.CharField(max_length=200)