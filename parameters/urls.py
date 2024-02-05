from django.urls import path
from . import views

urlpatterns=[
    # path('',views.index,name="parameter-list"),
    path('',views.ParameterListView.as_view(), name="parameter-list"),
    path('create/',  views.ParameterCreateView.as_view(), name='parameter-create'),
    path('update/',  views.ParameterUpdateView.as_view(), name='parameter-update'),
    path('delete/',  views.ParameterDeleteView.as_view(), name='parameter-delete'),

    path('thresholds',views.thresholds,name="threshold-list"),
    path('sensors',views.sensors,name="sensor-list"),
    path('landslides',views.landslides,name="landslide-list"),
    path('alerts',views.alerts,name="alert-list"),
]