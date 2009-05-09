from django import forms

class SearchForm(forms.Form):
    """The form used to receive queries"""
    query = forms.CharField(max_length=200)