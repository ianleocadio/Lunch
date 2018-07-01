from django import forms
from django.views.generic import FormView
from .utils.ajax import DayAjaxableResponseMixin, MonthAjaxableResponseMixin
from django.http import HttpResponseRedirect, JsonResponse
from app.models import Day, Month, Year

class DayForm(forms.Form):
    spent = forms.DecimalField(label="Spent",
                             widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
                             max_digits=7,
                             decimal_places=2)

class DayFormView(DayAjaxableResponseMixin, FormView):
    form_class = DayForm
    success_url = "/"

    def form_valid(self, form):
        # Chama primeiro o FORM_VALID do DayFormView
        response = super().form_valid(form)

        if isinstance(response, JsonResponse):
            return response

        day = self.kwargs["day"]
        month = self.kwargs["month"]
        year = self.kwargs["year"]
        dayObject = Day.objects.get(day=day, month__month=month, month__year__year=year)
        dayObject.spent = round(abs(float(form.data['spent'])), 2)
        dayObject.save()

        return HttpResponseRedirect('/days_by_month/'+str(year)+"/"+str(month))

    def form_invalid(self, form):
        # Chama primeiro o FORM_INVALID do DayFormView
        response = super().form_invalid(form)

        if isinstance(response, JsonResponse):
            return response

        return response



class MonthForm(forms.Form):
    balance = forms.DecimalField(label="Spent",
                             widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
                             max_digits=7,
                             decimal_places=2)

class MonthFormView(MonthAjaxableResponseMixin, FormView):
    form_class = MonthForm
    success_url = "/"

    def form_valid(self, form):
        # Chama primeiro o FORM_VALID do MonthFormView
        response = super().form_valid(form)
        if isinstance(response, JsonResponse):
            return response

        month = self.kwargs["month"]
        year = self.kwargs["year"]
        monthObj = Month.objects.get(month=month, year__year=year)
        monthObj.balance = round(float(form.data['balance']), 2)
        monthObj.save()

        return HttpResponseRedirect('/months_by_year')