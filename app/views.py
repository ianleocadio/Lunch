from django.shortcuts import render
from django.views.generic import ListView
from .models import Day, Month, Year
from .form.forms import DayForm

# Create your views here.


class YearList(ListView):
    model = Year
    template_name = "app/calendar.html"


class MonthView(ListView):
    model = Month
    template_name = "app/month.html"

    def get_queryset(self):
        list = Month.objects.filter(year__year=self.kwargs['year'])
        return list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["activeMonth"] = self.kwargs["month"]
        context['form'] = DayForm()
        return context
