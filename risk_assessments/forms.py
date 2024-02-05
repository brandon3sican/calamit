from django import forms  
from . import models
from factors.models import FactorRating

class RiskAssessmentForm(forms.ModelForm):  
    class Meta:  
        model = models.RiskAssessment  
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for select_tag in RiskAssessmentForm.base_fields.values(): 
            select_tag.empty_label = "--- Select ---"
        
        self.fields['vFactor'] = forms.ModelChoiceField(queryset = FactorRating.objects.filter(factor__short_name__iexact = 'vfactor'), empty_label = "--- Select ---")
        self.fields['fFactor'] = forms.ModelChoiceField(queryset = FactorRating.objects.filter(factor__short_name__iexact = 'ffactor'), empty_label = "--- Select ---")
        self.fields['sRed'] = forms.ModelChoiceField(queryset = FactorRating.objects.filter(factor__short_name__iexact = 'sred'), empty_label = "--- Select ---")
        self.fields['dRed'] = forms.ModelChoiceField(queryset = FactorRating.objects.filter(factor__short_name__iexact = 'dred'), empty_label = "--- Select ---")
        self.fields['lFactor'] = forms.ModelChoiceField(queryset = FactorRating.objects.filter(factor__short_name__iexact = 'lfactor'), empty_label = "--- Select ---")
        self.fields['sRating'] = forms.ModelChoiceField(queryset = FactorRating.objects.filter(factor__short_name__iexact = 'srating'), empty_label = "--- Select ---")
        self.fields['aRating'] = forms.ModelChoiceField(queryset = FactorRating.objects.filter(factor__short_name__iexact = 'arating'), empty_label = "--- Select ---")

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            
    def clean(self):
        cleaned_data = super(RiskAssessmentForm, self).clean()
        barangay = cleaned_data.get('barangay')
        landmark = cleaned_data.get('landmark')
        latitude = cleaned_data.get('latitude')
        longitude = cleaned_data.get('longitude')
        elevation = cleaned_data.get('elevation')
        vFactor = cleaned_data.get('vFactor')
        fFactor = cleaned_data.get('fFactor')
        sRed = cleaned_data.get('sRed')
        dRed = cleaned_data.get('dRed')
        lFactor = cleaned_data.get('lFactor')
        sRating = cleaned_data.get('sRating')
        aRating = cleaned_data.get('aRating')

        if not barangay:
            self.fields['barangay'].widget.attrs['class'] = 'form-control is-invalid'
        if not landmark:
            self.fields['landmark'].widget.attrs['class'] = 'form-control is-invalid'
        if not latitude:
            self.fields['latitude'].widget.attrs['class'] = 'form-control is-invalid'
        if not longitude:
            self.fields['longitude'].widget.attrs['class'] = 'form-control is-invalid'
        if not elevation:
            self.fields['elevation'].widget.attrs['class'] = 'form-control is-invalid'
        if not vFactor:
            self.fields['vFactor'].widget.attrs['class'] = 'form-control is-invalid'
        if not fFactor:
            self.fields['fFactor'].widget.attrs['class'] = 'form-control is-invalid'
        if not sRed:
            self.fields['sRed'].widget.attrs['class'] = 'form-control is-invalid'
        if not dRed:
            self.fields['dRed'].widget.attrs['class'] = 'form-control is-invalid'
        if not lFactor:
            self.fields['lFactor'].widget.attrs['class'] = 'form-control is-invalid'
        if not sRating:
            self.fields['sRating'].widget.attrs['class'] = 'form-control is-invalid'
        if not aRating:
            self.fields['aRating'].widget.attrs['class'] = 'form-control is-invalid'