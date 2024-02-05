from django import forms  
from . import models

class MunicipalityForm(forms.ModelForm):  
    class Meta:  
        model = models.Municipality  
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(MunicipalityForm, self).clean()
        municipality_name = cleaned_data.get('municipality_name')
        description = cleaned_data.get('description')
        contact_person = cleaned_data.get('contact_person')
        contact_number = cleaned_data.get('contact_number')

        if not municipality_name:
            self.fields['municipality_name'].widget.attrs['class'] = 'form-control is-invalid'
        if not description:
            self.fields['description'].widget.attrs['class'] = 'form-control is-invalid'
        if not contact_person:
            self.fields['contact_person'].widget.attrs['class'] = 'form-control is-invalid'
        if not contact_number:
            self.fields['contact_number'].widget.attrs['class'] = 'form-control is-invalid'