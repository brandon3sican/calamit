from django import forms  
from . import models

class FactorForm(forms.ModelForm):  
    class Meta:  
        model = models.Factor  
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(FactorForm, self).clean()
        factor_name = cleaned_data.get('factor_name')
        description = cleaned_data.get('description')

        if not factor_name:
            self.fields['factor_name'].widget.attrs['class'] = 'form-control is-invalid'
        if not description:
            self.fields['description'].widget.attrs['class'] = 'form-control is-invalid'

class FactorRatingForm(forms.ModelForm):  
    class Meta:  
        model = models.FactorRating  
        fields = "__all__"
        exclude = ('factor',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(FactorRatingForm, self).clean()
        factor_rating_name = cleaned_data.get('factor_rating_name')
        factor_rating_value = cleaned_data.get('factor_rating_value')

        if not factor_rating_name:
            self.fields['factor_rating_name'].widget.attrs['class'] = 'form-control is-invalid'
        if not factor_rating_value:
            self.fields['factor_rating_value'].widget.attrs['class'] = 'form-control is-invalid'