from django import forms
from parameters.models import Parameter
from django.forms import ModelChoiceField

class NameChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.parameter_name}'

class ThresholdForm(forms.Form):
    parameter = NameChoiceField(queryset=Parameter.objects.all(),empty_label="--- Select ---")
    upper_limit = forms.DecimalField(max_digits=10, decimal_places=2, label="Upper Limit")
    lower_limit = forms.DecimalField(max_digits=10, decimal_places=2, label="Lower Limit")
    description = forms.CharField(max_length=100)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(ThresholdForm, self).clean()
        parameter = cleaned_data.get('parameter')
        upper_limit = cleaned_data.get('upper_limit')
        lower_limit = cleaned_data.get('lower_limit')
        description = cleaned_data.get('description')
        if not parameter:
            self.fields['parameter'].widget.attrs['class'] = 'form-control is-invalid'
        if not upper_limit:
            self.fields['upper_limit'].widget.attrs['class'] = 'form-control is-invalid'
        if not lower_limit:
            self.fields['lower_limit'].widget.attrs['class'] = 'form-control is-invalid'
        if not description:
            self.fields['description'].widget.attrs['class'] = 'form-control is-invalid'
        

