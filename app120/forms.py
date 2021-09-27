from django import forms
from .models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields=['name','email','password']
        widgets={'password':forms.PasswordInput(render_value=True)}
