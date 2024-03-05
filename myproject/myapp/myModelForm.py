from django import forms
from .models import User
 
class UserForm(forms.ModelForm):
    class Meta:
      model = User
      fields = ['name', 'email', 'contact', 'country', 'date_of_birth']
      widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
    	}
