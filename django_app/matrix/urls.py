from django.urls import path 
from . import views


urlpatterns = [
    path("", views.main_page, name="base_page"),
    path("generate_table/", views.generate_matrix_table, name="generate_matrix_table"),
    path("simple_iteration_method/", views.simple_iteration_method),
    path("solve_by_simple_iteration_method/", views.solve_by_simple_iteration_method)
]