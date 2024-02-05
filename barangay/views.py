from django.shortcuts import render, redirect
from .models import Barangay
from .forms import BarangayForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models.functions import Lower
from django.db.models import Q

# Create your views here.
def index(request):
    if 'search' in request.GET:
        search_value = request.GET['search']
        query_result = Barangay.objects.filter(barangay_name__icontains = search_value)
        # multiple_q = Q(Q(term__icontains = query) | Q(definition__icontains = query))
        # glossary = Glossary.objects.filter(multiple_q)
    else:
        search_value = ""
        query_result = Barangay.objects.all().order_by(Lower('barangay_name'))

    paginator = Paginator(query_result, 10)
    page_number = request.GET.get("page")
    barangay = paginator.get_page(page_number)

    total_records = query_result.count()
    search_length = len(search_value)
    context = {'barangay':barangay,
                'total_records':total_records,
                'search_value':search_value,
                'search_length':search_length}

    return render(request,"barangay/barangay-list.html",context)

def add(request):
    form = BarangayForm()
    context = {
        'form' :  form,
        'heading' : 'Add Barangay',
        'button_label' : 'Save',
        'breadcrumb_active' : 'Add Barangay'
    }

    if request.method == "POST":  
        form = BarangayForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
            messages.success(request, 'Record Successfully Added')
            return redirect('barangay-list')

        else:
            context = {
                'form' :  form,
                'heading' : 'Add Barangay',
                'button_label' : 'Save',
                'breadcrumb_active' : 'Add Barangay'
            }

    return render(request,'barangay/barangay-add.html', context)

def show(request, barangay_id):
    try:
        data_selected = Barangay.objects.get(id = barangay_id)
        context = {'barangay':data_selected}
    except Barangay.DoesNotExist:
        return redirect('barangay-list')

    return render(request,'barangay/barangay-details.html',context)

def update(request, barangay_id):
    try:
        data_selected = Barangay.objects.get(id = barangay_id)
    except Barangay.DoesNotExist:
        return redirect('barangay-list')
    
    form = BarangayForm(request.POST or None, request.FILES or None, instance = data_selected)
    context = {
            'form' :  form,
            'heading' : 'Update Barangay',
            'button_label' : 'Save Changes',
            'breadcrumb_active' : 'Update Barangay'
    }

    if form.is_valid():
       form.save()
       messages.success(request, 'Record Successfully Updated')
       return redirect('barangay-list')

    return render(request,'barangay/barangay-add.html',context)

def delete(request, barangay_id):
    try:
        data_selected = Barangay.objects.get(id = barangay_id)
    except Barangay.DoesNotExist:
        return redirect('barangay-list')
    data_selected.delete()
    messages.success(request, 'Record Permanently Deleted')
    return redirect('barangay-list')