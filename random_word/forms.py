from django import forms
from random_word.models import Vocabulary

class WordModelForm(forms.ModelForm):
    class Meta:
        model=Vocabulary
        fields='__all__'
        
        
