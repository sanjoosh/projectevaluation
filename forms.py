from django import forms

from .models import ProjectEvaluation

class LoginForm(forms.ModelForm):
    class Meta:
        model=ProjectEvaluation
   

 
  