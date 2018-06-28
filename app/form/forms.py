from django import forms
from django.views.generic import FormView
from .utils.ajax import DayAjaxableResponseMixin, MonthAjaxableResponseMixin

class DayForm(forms.Form):
    spent = forms.DecimalField(label="Spent",
                             widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
                             max_digits=7,
                             decimal_places=2)

class DayFormView(DayAjaxableResponseMixin, FormView):
    form_class = DayForm
    success_url = "/"



class MonthForm(forms.Form):
    balance = forms.DecimalField(label="Spent",
                             widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
                             max_digits=7,
                             decimal_places=2)

class MonthFormView(MonthAjaxableResponseMixin, FormView):
    form_class = MonthForm
    success_url = "/"