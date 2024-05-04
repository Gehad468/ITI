from django import forms
from auther.models import Author
from.models import *


class Addbook(forms.Form):
    title=forms.CharField(required=True)
    version=forms.NumberInput()
    author=forms.ChoiceField(choices=Author.get_all())
 

class AddBookModel(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'



