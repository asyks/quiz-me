from django import forms
from django.forms import ModelForm
from .models import CHOICES_UNITS, Attempt, Schedule

from pagedown.widgets import PagedownWidget


class FormAttemptNew(forms.Form):
    attempt  = forms.CharField(label="A", required=False, widget=PagedownWidget())


class ModelFormSchedule(ModelForm):
    class Meta:
        model = Schedule
        fields = ('date_show_next', 'interval_num', 'interval_unit')


class FormSchedule(forms.Form):
    interval_num = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    interval_unit = forms.ChoiceField(choices=CHOICES_UNITS)
