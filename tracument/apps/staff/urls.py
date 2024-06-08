from django.urls import path
from . import views

urlpatterns = [
    path('staff-by-unit', views.staff_by_unit, name="staff-by-unit"),
    path('staff-list', views.staff_list, name="staff-list"),
]
