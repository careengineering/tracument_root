from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Staff, Unit
from .forms import StaffForm

# Staff List
def staff_list(request):
    staffs = Staff.objects.all().select_related('unit', 'payroll').prefetch_related('duty')
    context = {'staffs': staffs}
    return render(request, 'staff/staff_list.html', context)

# Create Staff
def staff_create(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff-list')
    else:
        form = StaffForm()
    return render(request, 'staff/staff_form.html', {'form': form})

# Update Staff
def staff_update(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff-list')
    else:
        form = StaffForm(instance=staff)
    return render(request, 'staff/staff_form.html', {'form': form})

# Delete Staff
def staff_delete(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff.delete()
        return redirect('staff-list')
    return render(request, 'staff/staff_confirm_delete.html', {'staff': staff})

# Staff List by Unit
def staff_by_unit(request):
    units = Unit.objects.all()
    unit_staffs = {}
    for unit in units:
        staff = Staff.objects.filter(unit=unit).select_related('title').prefetch_related('duty').order_by('-title__name')
        unit_staffs[unit] = staff
    context = {'unit_staffs': unit_staffs}
    return render(request, 'staff/staff-by-unit.html', context)

# Staff List by Unit - printable
def printable_staff_by_unit(request):
    units = Unit.objects.all()
    unit_staffs = {}
    for unit in units:
        staff = Staff.objects.filter(unit=unit).select_related('title').prefetch_related('duty').order_by('-title__name')
        unit_staffs[unit] = staff
    context = {'unit_staffs': unit_staffs}
    return render(request, 'staff/printable-staff-by-unit.html', context)


