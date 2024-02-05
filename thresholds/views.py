from django.shortcuts import render
from django.views.generic import ListView, View
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from . import models
from parameters.models import Parameter
from . import forms

# Create your views here.
def index(request):
    return render(request,"thresholds/threshold-list.html")

class ThresholdListView(ListView):
    queryset = models.Threshold.objects.select_related('parameter').all()
    template_name = 'thresholds/threshold-list.html'
    context_object_name = 'thresholds'

    def get_context_data(self, **kwargs):
        context = super(ThresholdListView, self).get_context_data(**kwargs)
        context['parameters'] = Parameter.objects.all() 
        # context['third_queryset'] = # YOUR QUERY HERE
        return context
    
class ThresholdCreateView(View):
    def get(self, request):
        parameter1 = request.GET.get('parameter', None)
        lower_limit1 = request.GET.get('lower_limit', None)
        upper_limit1 = request.GET.get('upper_limit', None)
        description1 = request.GET.get('description', None)

        obj = models.Threshold.objects.create(
            parameter_id = parameter1,
            lower_limit = lower_limit1,
            upper_limit = upper_limit1,
            description = description1
        )

        obj2 = Parameter.objects.get(pk=parameter1) 
        
        threshold = {'id':obj.id,'parameter':obj.parameter_id,'lower_limit':obj.lower_limit,'upper_limit':obj.upper_limit,'description':obj.description}
        parameter = {'id':obj2.id,'parameter_name':obj2.parameter_name,'description':obj2.description,'measurement_unit':obj2.measurement_unit}
        data = {
                'threshold': threshold,'parameter':parameter
        }

        return JsonResponse(data)
    

def index_test(request):
    if request.method=='POST':
         form = forms.ThresholdForm(request.POST)
         if form.is_valid():
             pass
    else:
         form = forms.ThresholdForm()

    thresholds = models.Threshold.objects.select_related('parameter')
    context = {
        'thresholds': thresholds,
        'form':form,
    }

    return render(request,"thresholds/threshold-test.html", context)

def threshold_create(request):
    form = forms.ThresholdForm()
    context = {
        'form':form,
    }
    html_form = render_to_string('thresholds/threshold-form.html',
        context,
        request = request,
    )
      
    return JsonResponse({'html_form':html_form})


