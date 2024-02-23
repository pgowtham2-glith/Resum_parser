from django import forms
from .models import StudentForm
class UploadForm(forms.ModelForm):
    class Meta:
        model=StudentForm
        fields=['file']