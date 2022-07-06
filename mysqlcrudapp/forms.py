import control as control
import form as form
from django import forms
from mysqlcrudapp.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields = '__all__'
        widgets = {
            'uname': forms.TextInput(attrs={'class':'form - control'}),
            'uemail': forms.TextInput(attrs={'class':'form - control'}),
            'upassword': forms.PasswordInput(attrs={'class':'form - control'})
        }