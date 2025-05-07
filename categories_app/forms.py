
from django import forms
from django.core.exceptions import ValidationError
from .models import Category
# from models import ErrorCategory

class ErrorCategoryForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        category_required = cleaned_data.get('Category').requires_description
        description = cleaned_data.get('description')

        if category_required and not description:
            raise ValidationError("A categoria seleciona exige o preenchimento da descrição .")
        return cleaned_data
