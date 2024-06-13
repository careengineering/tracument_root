from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Staff, Unit, Title, Payroll, Duty
from .forms import StaffForm, StaffFilterForm
from django.db.models import Q
from django.contrib import messages

# Staff List
def staff_list(request):
    form = StaffFilterForm(request.GET or None)
    staffs = Staff.objects.all()

    if form.is_valid():
        query = form.cleaned_data.get('q')
        name = form.cleaned_data.get('name')
        surname = form.cleaned_data.get('surname')
        unit = form.cleaned_data.get('unit')
        title = form.cleaned_data.get('title')
        payroll = form.cleaned_data.get('payroll')
        duty_ids = form.cleaned_data.get('duty')
        is_active = form.cleaned_data.get('is_active')

        if query:
            staffs = staffs.filter(
                Q(name__icontains=query) |
                Q(surname__icontains=query) |
                Q(unit__name__icontains=query) |
                Q(title__name__icontains=query) |
                Q(payroll__name__icontains=query) |
                Q(duty__name__icontains=query)
            ).distinct()
        if name:
            staffs = staffs.filter(name__icontains=name)
        if surname:
            staffs = staffs.filter(surname__icontains=surname)
        if unit:
            staffs = staffs.filter(unit=unit)
        if title:
            staffs = staffs.filter(title=title)
        if payroll:
            staffs = staffs.filter(payroll=payroll)
        if duty_ids:
            staffs = staffs.filter(duty__in=duty_ids)
        if is_active != '':
            staffs = staffs.filter(is_active=is_active)

    context = {
        'staffs': staffs,
        'form': form,
        'staff_count': staffs.count()
    }
    return render(request, 'staff/staff-list.html', context)

# Create Staff
def staff_create(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff-list')
    else:
        form = StaffForm()
    return render(request, 'staff/staff-form.html', {'form': form})

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
    return render(request, 'staff/staff-form.html', {'form': form})

# Delete Staff
def staff_delete(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff.delete()
        messages.success(request, 'Silme işlemi başarılı')
        return redirect('staff-list')
    return redirect('staff-list')

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


