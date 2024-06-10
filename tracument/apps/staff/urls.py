from django.urls import path
from . import views

urlpatterns = [
    path('staff/', views.staff_list, name='staff-list'),
    path('staff/create/', views.staff_create, name='staff-create'),
    path('staff/update/<int:pk>/', views.staff_update, name='staff-update'),
    path('staff/delete/<int:pk>/', views.staff_delete, name='staff-delete'),
    path('staff-by-unit', views.staff_by_unit, name="staff-by-unit"),
    path('printable-staff-by-unit/', views.printable_staff_by_unit, name="printable-staff-by-unit"),
]
