from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="barangay-list"),
    path('add/', views.add, name ="barangay-add"),
    path('show/<int:barangay_id>', views.show, name="barangay-details"),
    path('update/<int:barangay_id>', views.update),
    path('delete/<int:barangay_id>', views.delete, name="barangay-delete"),
] 