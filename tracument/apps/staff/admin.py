from django.contrib import admin
from .models import Unit, Title, Duty, Payroll, Staff


# For staff
class UnitAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class TitleAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class DutyAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class PayrollAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

class StaffAdmin(admin.ModelAdmin):
    list_display = ("full_name_with_title", "unit", "payroll", "display_duty")
    # search_fields = ("name", "surname", "unit", "payroll", "title", "display_duty")
    list_filter = ("unit", "payroll", "title", "duty")

    def full_name_with_title(self, obj):
        if str(obj.title).strip() == "-":
            return f"{obj.name.upper()} {obj.surname.upper()}"
        else:
            return f"{obj.name.upper()} {obj.surname.upper()} ({obj.title})"

    full_name_with_title.short_description = 'İsim ve Soyisim'

    def display_duty(self, obj):
        return ", ".join([duty.name for duty in obj.duty.all()])


admin.site.register(Staff, StaffAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Duty, DutyAdmin)
admin.site.register(Payroll, PayrollAdmin)

