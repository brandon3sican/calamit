from django.urls import path
from . import views

urlpatterns=[
    # path('',views.index,name="threshold-list"),
    path('',views.ThresholdListView.as_view(), name="threshold-list"),
    path('create/',  views.ThresholdCreateView.as_view(), name='threshold-create'),
    # path('update/',  views.ParameterUpdateView.as_view(), name='parameter-update'),
    # path('delete/',  views.ParameterDeleteView.as_view(), name='parameter-delete'),
    path('test/',views.index_test, name="threshold-test"),
    path('create/', views.threshold_create, name='threshold-create'),
    # path('test/',views.ThresholdListView2.as_view(), name="threshold-test"),
]