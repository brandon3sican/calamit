from django import forms  
from . import models

class GlossaryForm(forms.ModelForm):  
    class Meta:  
        model = models.Glossary  
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(GlossaryForm, self).clean()
        term = cleaned_data.get('term')
        definition = cleaned_data.get('definition')

        if not term:
            self.fields['term'].widget.attrs['class'] = 'form-control is-invalid'
        if not definition:
            self.fields['definition'].widget.attrs['class'] = 'form-control is-invalid'