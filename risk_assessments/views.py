from django.shortcuts import render, redirect
from .models import RiskAssessment
from factors.models import FactorRating
from .forms import RiskAssessmentForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models.functions import Lower
from django.db.models import Q

# Create your views here.
def index(request):
    if 'search' in request.GET:
        search_value = request.GET['search']
        query_result = RiskAssessment.objects.filter(landmark__icontains = search_value)
        # multiple_q = Q(Q(term__icontains = query) | Q(definition__icontains = query))
        # glossary = Glossary.objects.filter(multiple_q)
    else:
        search_value = ""
        query_result = RiskAssessment.objects.all()

    paginator = Paginator(query_result, 10)
    page_number = request.GET.get("page")
    risk_assessment = paginator.get_page(page_number)

    total_records = query_result.count()
    search_length = len(search_value)
    context = {'risk_assessment':risk_assessment,
                'total_records':total_records,
                'search_value':search_value,
                'search_length':search_length}

    return render(request,"risk_assessment/risk-assessment-list.html",context)

def add(request):
    form = RiskAssessmentForm()
    context = {
        'form' :  form,
        'heading' : 'Add Risk Assessment',
        'button_label' : 'Save',
        'breadcrumb_active' : 'Add Risk Assessment'
    }

    if request.method == "POST":  
        form = RiskAssessmentForm(request.POST, request.FILES)  
        if form.is_valid():
            # vfactor = FactorRating.objects.get(id=request.POST.get("vFactor")).factor_rating_value
            # ffactor = FactorRating.objects.get(id=request.POST.get("fFactor")).factor_rating_value
            # sred = FactorRating.objects.get(id=request.POST.get("sRed")).factor_rating_value
            # dred = FactorRating.objects.get(id=request.POST.get("dRed")).factor_rating_value
            # lfactor = FactorRating.objects.get(id=request.POST.get("lFactor")).factor_rating_value
            # srating = FactorRating.objects.get(id=request.POST.get("sRating")).factor_rating_value
            # arating = FactorRating.objects.get(id=request.POST.get("aRating")).factor_rating_value

            # print(f'vfactor = {vfactor} \n ffactor = {ffactor} \n sred = {sred} \n dred = {dred} \n lfactor = {lfactor} \n srating = {srating} \n arating = {arating}')

            # fs = (vfactor * ffactor * (srating - sred - dred)) / (arating * lfactor)
            # if fs > 1.2 :
            #     fs_result = "Stable"
            # elif fs > 1.0 and fs <= 1.2 :
            #     fs_result = "Marginally Stable"
            # elif fs > 0.7 and fs <= 1.0 :
            #     fs_result = "Susceptible"
            # elif fs <= 0.7 :
            #     fs_result = "Highly Susceptible"

            # print(f'factor of safety = {fs} \n fs_result = {fs_result}')
            
            new_risk_assessment = form.save()
            messages.success(request, 'Record Successfully Added')
            return redirect('risk-assessment-details', new_risk_assessment.pk)

        else:
            context = {
                'form' :  form,
                'heading' : 'Add Risk Assessment',
                'button_label' : 'Save',
                'breadcrumb_active' : 'Add Risk Assessment'
            }

    return render(request,'risk_assessment/risk-assessment-add.html', context)

def show(request, risk_assessment_id):
    try:
        data_selected = RiskAssessment.objects.get(id = risk_assessment_id)

        vfactor = data_selected.vFactor.factor_rating_value
        ffactor = data_selected.fFactor.factor_rating_value
        sred = data_selected.sRed.factor_rating_value
        dred = data_selected.dRed.factor_rating_value
        lfactor = data_selected.lFactor.factor_rating_value
        srating = data_selected.sRating.factor_rating_value
        arating = data_selected.aRating.factor_rating_value

        # print(f'vfactor = {vfactor} \n ffactor = {ffactor} \n sred = {sred} \n dred = {dred} \n lfactor = {lfactor} \n srating = {srating} \n arating = {arating}')

        factor_of_safety = (vfactor * ffactor * (srating - sred - dred)) / (arating * lfactor)

        if factor_of_safety > 1.2 :
            fs_result = "Stable"
        elif factor_of_safety > 1.0 and factor_of_safety <= 1.2 :
            fs_result = "Marginally Stable"
        elif factor_of_safety > 0.7 and factor_of_safety <= 1.0 :
            fs_result = "Susceptible"
        elif factor_of_safety <= 0.7 :
            fs_result = "Highly Susceptible"
        
        # print(f'factor of safety = {factor_of_safety} \n fs_result = {fs_result}')
        
        context = { 'risk_assessment' : data_selected,
                    'factor_of_safety' : round(factor_of_safety,4),
                    'fs_result' : fs_result }

    except FactorRating.DoesNotExist:
        return redirect('risk-assessment-list')

    return render(request,'risk_assessment/risk-assessment-details.html',context)

def update(request, risk_assessment_id):
    try:
        data_selected = RiskAssessment.objects.get(id = risk_assessment_id)
    except RiskAssessment.DoesNotExist:
        return redirect('risk-assessment-list')
    
    form = RiskAssessmentForm(request.POST or None, request.FILES or None, instance = data_selected)
    context = {
            'form' :  form,
            'heading' : 'Update Risk Assessment',
            'button_label' : 'Save Changes',
            'breadcrumb_active' : 'Update Risk Assessment'
    }

    if form.is_valid():
       form.save()
       messages.success(request, 'Record Successfully Updated')
       return redirect('risk-assessment-details', risk_assessment_id)

    return render(request,'risk_assessment/risk-assessment-add.html',context)
    
def delete(request, risk_assessment_id):
    try:
        data_selected = RiskAssessment.objects.get(id = risk_assessment_id)
    except RiskAssessment.DoesNotExist:
        return redirect('risk-assessment-list')
    data_selected.delete()
    messages.success(request, 'Record Permanently Deleted')
    return redirect('risk-assessment-list')