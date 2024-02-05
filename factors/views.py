from django.shortcuts import render, redirect
from .models import Factor
from .models import FactorRating
from .forms import FactorForm
from .forms import FactorRatingForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models.functions import Lower
from django.db.models import Q

# Create your views here.
def index(request):
    if 'search' in request.GET:
        search_value = request.GET['search']
        query_result = Factor.objects.filter(factor_name__icontains = search_value)
        # multiple_q = Q(Q(term__icontains = query) | Q(definition__icontains = query))
        # glossary = Glossary.objects.filter(multiple_q)
    else:
        search_value = ""
        query_result = Factor.objects.all().order_by(Lower('factor_name'))

    paginator = Paginator(query_result, 10)
    page_number = request.GET.get("page")
    factor = paginator.get_page(page_number)

    total_records = query_result.count()
    search_length = len(search_value)
    context = {'factor':factor,
                'total_records':total_records,
                'search_value':search_value,
                'search_length':search_length}

    return render(request,"factor/factor-list.html",context)

def add(request):
    form = FactorForm()
    context = {
        'form' :  form,
        'heading' : 'Add Factor',
        'button_label' : 'Save',
        'breadcrumb_active' : 'Add Factor'
    }

    if request.method == "POST":  
        form = FactorForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
            messages.success(request, 'Record Successfully Added')
            return redirect('factor-list')

        else:
            context = {
                'form' :  form,
                'heading' : 'Add Factor',
                'button_label' : 'Save',
                'breadcrumb_active' : 'Add Factor'
            }

    return render(request,'factor/factor-add.html', context)  

# this shows the factor details including the ratings
def show(request, factor_id):
    try:
        data_selected = Factor.objects.get(id = factor_id)
        # Select * from factor_rating where factor = ?
        factor_rating = FactorRating.objects.filter(factor=factor_id).values().order_by('-factor_rating_value')
        total_records = factor_rating.count()
        
        context = {'factor':data_selected,
                    'factor_rating': factor_rating,
                    'total_records': total_records}
    except Factor.DoesNotExist:
        return redirect('factor-list')

    return render(request,'factor/factor-details.html',context)

def update(request, factor_id):
    try:
        data_selected = Factor.objects.get(id = factor_id)
    except Factor.DoesNotExist:
        return redirect('factor-list')
    
    form = FactorForm(request.POST or None, request.FILES or None, instance = data_selected)
    context = {
            'form' :  form,
            'heading' : 'Update Factor',
            'button_label' : 'Save Changes',
            'breadcrumb_active' : 'Update Factor'
    }

    if form.is_valid():
       form.save()
       messages.success(request, 'Record Successfully Updated')
       return redirect('factor-list')

    return render(request,'factor/factor-add.html',context)

def delete(request, factor_id):
    try:
        data_selected = Factor.objects.get(id = factor_id)
    except Factor.DoesNotExist:
        return redirect('factor-list')
    
    if request.method == 'POST':
        try:
            data_selected.delete()
            messages.success(request, 'Record Permanently Deleted')
        except Exception:
            messages.error(request, 'An error occured, unable to delete selected data.')
            return redirect('factor-list')

    return redirect('factor-list')

# --------------- FACTOR RATING ------------- #
# FACTOR RATING - ADD
def add_factor_rating(request, factor_id):
    form = FactorRatingForm()
    factor = Factor.objects.get(id = factor_id)
    context = {
        'form' :  form,
        'heading' : 'Add Factor Rating',
        'button_label' : 'Save',
        'breadcrumb_active' : 'Add Factor Rating',
        'factor' : factor,
    }

    if request.method == "POST":  
        form = FactorRatingForm(request.POST, request.FILES)  
        if form.is_valid():
            form.instance.factor_id = factor_id
            form.save()
            messages.success(request, 'Record Successfully Added')
            return redirect('factor-details', factor_id)

        else:
            context = {
                'form' :  form,
                'heading' : 'Add Factor Rating',
                'button_label' : 'Save',
                'breadcrumb_active' : 'Add Factor Rating',
                'factor' : factor,
            }

    return render(request,'factor/factor-rating-add.html', context)

# FACTOR RATING - UPDATE
def update_factor_rating(request, factor_rating_id):
    try:
        data_selected = FactorRating.objects.get(id = factor_rating_id)
    except FactorRating.DoesNotExist:
        return redirect('factor-list')
    
    form = FactorRatingForm(request.POST or None, request.FILES or None, instance = data_selected)
    context = {
            'form' :  form,
            'heading' : 'Update Factor Rating',
            'button_label' : 'Save',
            'breadcrumb_active' : 'Update Factor Rating',
            'factor' : {'id' : data_selected.factor_id,
                        'factor_name' : data_selected.factor.factor_name}
    }

    if form.is_valid():
       form.save()
       messages.success(request, 'Record Successfully Updated')
       return redirect('factor-details', data_selected.factor_id)

    return render(request,'factor/factor-rating-add.html',context)

# FACTOR RATING - DELETE
def delete_factor_rating(request, factor_rating_id):
    try:
        data_selected = FactorRating.objects.get(id = factor_rating_id)
    except FactorRating.DoesNotExist:
        return redirect('factor-details', data_selected.factor_id)
    data_selected.delete()
    messages.success(request, 'Record Permanently Deleted')
    return redirect('factor-details', data_selected.factor_id)