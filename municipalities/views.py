from django.shortcuts import render, redirect
from .models import Municipality
from .forms import MunicipalityForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models.functions import Lower
from django.db.models import Q

# Create your views here.
def index(request):
    if 'search' in request.GET:
        search_value = request.GET['search']
        query_result = Municipality.objects.filter(municipality_name__icontains = search_value)
        # multiple_q = Q(Q(term__icontains = query) | Q(definition__icontains = query))
        # glossary = Glossary.objects.filter(multiple_q)
    else:
        search_value = ""
        query_result = Municipality.objects.all().order_by(Lower('municipality_name'))

    paginator = Paginator(query_result, 10)
    page_number = request.GET.get("page")
    municipality = paginator.get_page(page_number)

    total_records = query_result.count()
    search_length = len(search_value)
    context = {'municipality':municipality,
                'total_records':total_records,
                'search_value':search_value,
                'search_length':search_length}

    return render(request,"municipality/municipality-list.html",context)

def add(request):
    form = MunicipalityForm()
    context = {
        'form' :  form,
        'heading' : 'Add Municipality',
        'button_label' : 'Save',
        'breadcrumb_active' : 'Add Municipality'
    }

    if request.method == "POST":  
        form = MunicipalityForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
            messages.success(request, 'Record Successfully Added')
            return redirect('municipality-list')

        else:
            context = {
                'form' :  form,
                'heading' : 'Add Municipality',
                'button_label' : 'Save',
                'breadcrumb_active' : 'Add Municipality'
            }

    return render(request,'municipality/municipality-add.html', context)  

def show(request, municipality_id):
    try:
        data_selected = Municipality.objects.get(id = municipality_id)
        context = {'municipality':data_selected}
    except Municipality.DoesNotExist:
        return redirect('municipality-list')

    return render(request,'municipality/municipality-details.html',context)

def update(request, municipality_id):
    try:
        data_selected = Municipality.objects.get(id = municipality_id)
    except Municipality.DoesNotExist:
        return redirect('municipality-list')
    
    form = MunicipalityForm(request.POST or None, request.FILES or None, instance = data_selected)
    context = {
            'form' :  form,
            'heading' : 'Update Municipality',
            'button_label' : 'Save Changes',
            'breadcrumb_active' : 'Update Municipality'
    }

    if form.is_valid():
       form.save()
       messages.success(request, 'Record Successfully Updated')
       return redirect('municipality-list')

    return render(request,'municipality/municipality-add.html',context)

def delete(request, municipality_id):
    try:
        data_selected = Municipality.objects.get(id = municipality_id)
    except Municipality.DoesNotExist:
        return redirect('municipality-list')
    data_selected.delete()
    messages.success(request, 'Record Permanently Deleted')
    return redirect('municipality-list')

