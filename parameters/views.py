from django.shortcuts import render
from django.views.generic import ListView, View
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models


# Create your views here.
# def index(request):
    # return render(request,"parameters/parameter-list.html")
    
class ParameterListView(LoginRequiredMixin, ListView):
    model = models.Parameter
    template_name = 'parameters/parameter-list.html'
    context_object_name = 'parameters'
    ordering = ['parameter_name']
    paginate_by = 10

class ParameterCreateView(View):
    def get(self, request):
        parameter_name1 = request.GET.get('parameter_name', None)
        description1 = request.GET.get('description', None)
        measurement_unit1 = request.GET.get('measurement_unit', None)

        obj = models.Parameter.objects.create(
            parameter_name = parameter_name1,
            description = description1,
            measurement_unit = measurement_unit1
        )

        parameter = {'id':obj.id,'parameter_name':obj.parameter_name,'description':obj.description,'measurement_unit':obj.measurement_unit}

        data = {
              'parameter': parameter
        }
        return JsonResponse(data)
    
class ParameterUpdateView(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        parameter_name1 = request.GET.get('parameter_name', None)
        description1 = request.GET.get('description', None)
        measurement_unit1 = request.GET.get('measurement_unit', None)

        obj = models.Parameter.objects.get(id=id1)
        obj.parameter_name = parameter_name1
        obj.description = description1
        obj.measurement_unit = measurement_unit1
        obj.save()

        parameter = {'id':obj.id,'parameter_name':obj.parameter_name,'description':obj.description,'measurement_unit':obj.measurement_unit}

        data = {
            'parameter': parameter
        }
        return JsonResponse(data)
    
class ParameterDeleteView(View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        models.Parameter.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

def thresholds(request):
    return render(request,"parameters/threshold-list.html")

def sensors(request):
    return render(request,"parameters/sensor-list.html")

def landslides(request):
    return render(request,"parameters/landslide-list.html")

def alerts(request):
    return render(request,"parameters/alerts-list.html")