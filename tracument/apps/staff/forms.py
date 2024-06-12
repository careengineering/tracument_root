from django import forms
from .models import Staff,Unit, Title, Payroll, Duty


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'surname', 'payroll', 'unit', 'title', 'duty', 'is_active']

class StaffFilterForm(forms.Form):
    q = forms.CharField(label='Genel Arama', required=False)
    name = forms.CharField(label='Ad', required=False)
    surname = forms.CharField(label='Soyad', required=False)
    unit = forms.ModelChoiceField(queryset=Unit.objects.all(), label='Birim', required=False)
    title = forms.ModelChoiceField(queryset=Title.objects.all(), label='Unvan', required=False)
    payroll = forms.ModelChoiceField(queryset=Payroll.objects.all(), label='Kadro', required=False)
    duty = forms.ModelChoiceField(queryset=Duty.objects.all(), label='Görev', required=False)
    is_active = forms.ChoiceField(
        choices=[('', 'Tümü'), (True, 'Aktif'), (False, 'Pasif')],
        label='Durum',
        required=False
    )

    def clean(self):
        cleaned_data = super().clean()
        for field_name in ['q', 'name', 'surname']:
            value = cleaned_data.get(field_name)
            if value:
                value = value.upper()
                cleaned_data[field_name] = value
        return cleaned_data