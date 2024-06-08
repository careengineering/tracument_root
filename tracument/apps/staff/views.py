from django.shortcuts import render
from .models import Staff, Unit

# - Staff list
def staff_list(request):
    staffs = Staff.objects.all().select_related('unit','payroll').prefetch_related('duty')
    context = {'stafFs':staffs}
    return render(request,'staff/staff_list.html', context=context)

def staff_by_unit(request):
    units = Unit.objects.all()
    unit_staffs = {}
    for unit in units:
        staff = Staff.objects.filter(unit=unit).select_related('title').prefetch_related('duty').order_by('-title__name')
        unit_staffs[unit] = staff
    context = {'unit_staffs': unit_staffs}
    return render(request, 'staff/staff-by-unit.html', context)