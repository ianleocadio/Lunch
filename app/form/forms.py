from django import forms
from django.views.generic import FormView
from .utils.ajax import DayAjaxableResponseMixin

class DayForm(forms.Form):
    spent = forms.DecimalField(label="Spent",
                             widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
                             max_digits=5,
                             decimal_places=2)

class DayFormView(DayAjaxableResponseMixin, FormView):
    form_class = DayForm
    success_url = "/"
