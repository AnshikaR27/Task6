from django import forms
from .models import VisaApplication

class VisaApplicationForm(forms.ModelForm):
    class Meta:
        model = VisaApplication
        fields = ['age', 'income', 'previous_travel', 'documents_complete']