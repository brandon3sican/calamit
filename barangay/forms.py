from django import forms  
from . import models

class BarangayForm(forms.ModelForm):  
    class Meta:
        model = models.Barangay  
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(BarangayForm, self).clean()
        barangay_name = cleaned_data.get('barangay_name')
        municipality = cleaned_data.get('municipality')
        description = cleaned_data.get('description')
        contact_person = cleaned_data.get('contact_person')
        contact_number = cleaned_data.get('contact_number')

        if not barangay_name:
            self.fields['barangay_name'].widget.attrs['class'] = 'form-control is-invalid'
        if not municipality:
            self.fields['municipality'].widget.attrs['class'] = 'form-control is-invalid'
        if not description:
            self.fields['description'].widget.attrs['class'] = 'form-control is-invalid'
        if not contact_person:
            self.fields['contact_person'].widget.attrs['class'] = 'form-control is-invalid'
        if not contact_number:
            self.fields['contact_number'].widget.attrs['class'] = 'form-control is-invalid'