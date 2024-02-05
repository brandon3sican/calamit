from django.urls import path
from . import views

urlpatterns=[
     # url factor
    path('',views.index,name="factor-list"),
    path('add/', views.add, name = 'factor-add'),
    path('show/<int:factor_id>', views.show, name="factor-details"),
    path('update/<int:factor_id>', views.update, name="factor-update"),
    path('delete/<int:factor_id>', views.delete, name="factor-delete"),

    # url of factor ratings for each of the factors
    path('rating/add/<int:factor_id>', views.add_factor_rating, name = 'factor-rating-add'),
    path('rating/update/<int:factor_rating_id>', views.update_factor_rating, name="factor-rating-update"),
    path('rating/delete/<int:factor_rating_id>', views.delete_factor_rating, name="factor-rating-delete"),
]