from django import forms
from .utils.ajax import AjaxableResponseMixin


class DayForm(AjaxableResponseMixin, forms.Form):
    spent = forms.FloatField(label="Gasto", widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
    day = forms.HiddenInput()
    month = forms.HiddenInput()
    year = forms.HiddenInput()
