from django import forms
from .models import Schedule


class ScheduleForm(forms.ModelForm):  # Model(input) => Form(output)
    class Meta:
        model = Schedule
        fields = '__all__'