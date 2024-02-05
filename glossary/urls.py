from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="glossary-list"),
    path('add/', views.add, name = 'glossary-add'),
    path('show/<int:glossary_id>', views.show, name="glossary-details"),
    path('update/<int:glossary_id>', views.update),
    path('delete/<int:glossary_id>', views.delete, name="glossary-delete"),
]