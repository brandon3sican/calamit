from django.shortcuts import render, redirect
from .models import Glossary
from .forms import GlossaryForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models.functions import Lower
from django.db.models import Q

# Create your views here.
def index(request):
    if 'search' in request.GET:
        search_value = request.GET['search']
        query_result = Glossary.objects.filter(term__icontains = search_value)
        # multiple_q = Q(Q(term__icontains = query) | Q(definition__icontains = query))
        # glossary = Glossary.objects.filter(multiple_q)
    else:
        search_value = ""
        query_result = Glossary.objects.all().order_by(Lower('term'))

    paginator = Paginator(query_result, 10)
    page_number = request.GET.get("page")
    glossary = paginator.get_page(page_number)

    total_records = query_result.count()
    search_length = len(search_value)
    context = {'glossary':glossary,
                'total_records':total_records,
                'search_value':search_value,
                'search_length':search_length}

    return render(request,"glossary/glossary-list.html",context)

def add(request):
    form = GlossaryForm()
    context = {
        'form' :  form,
        'heading' : 'Add Glossary Term',
        'button_label' : 'Save',
        'breadcrumb_active' : 'Add Term'
    }

    if request.method == "POST":  
        form = GlossaryForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save() 
            messages.success(request, 'Record Successfully Added')
            return redirect('glossary-list')

        else:
            context = {
                'form' :  form,
                'heading' : 'Add Glossary Term',
                'button_label' : 'Save',
                'breadcrumb_active' : 'Add Term'
            }

    return render(request,'glossary/glossary-add.html', context)  

def show(request, glossary_id):
    try:
        data_selected = Glossary.objects.get(id = glossary_id)
        context = {'glossary':data_selected}
    except Glossary.DoesNotExist:
        return redirect('glossary-list')

    return render(request,'glossary/glossary-details.html',context)

def update(request, glossary_id):
    try:
        data_selected = Glossary.objects.get(id = glossary_id)
    except Glossary.DoesNotExist:
        return redirect('glossary-list')
    
    form = GlossaryForm(request.POST or None, request.FILES or None, instance = data_selected)
    context = {
            'form' :  form,
            'heading' : 'Update Glossary Term',
            'button_label' : 'Save Changes',
            'breadcrumb_active' : 'Update Term'
    }

    if form.is_valid():
       form.save()
       messages.success(request, 'Record Successfully Updated')
       return redirect('glossary-list')

    return render(request,'glossary/glossary-add.html',context)

def delete(request, glossary_id):
    try:
        data_selected = Glossary.objects.get(id = glossary_id)
    except Glossary.DoesNotExist:
        return redirect('glossary-list')
    data_selected.delete()
    messages.success(request, 'Record Permanently Deleted')
    return redirect('glossary-list')

