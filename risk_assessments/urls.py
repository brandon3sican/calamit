from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="risk-assessment-list"),
    path('add/', views.add, name = 'risk-assessment-add'),
    path('show/<int:risk_assessment_id>', views.show, name="risk-assessment-details"),
    path('update/<int:risk_assessment_id>', views.update, name = 'risk-assessment-update'),
    path('delete/<int:risk_assessment_id>', views.delete, name="risk-assessment-delete"),
]