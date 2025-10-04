from django.urls import path 
from . import views


urlpatterns = [
    path("", views.main_page, name="base_page"),
    path("generate_table/", views.matrix_table, name="matrix_table")
]