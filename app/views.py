from django.views.generic import ListView
from .models import Day, Month, Year
from .form.forms import DayFormView
import datetime
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

@method_decorator(login_required, name='dispatch')
class YearList(ListView):
    model = Year
    template_name = "app/calendar.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["activeMonth"] = datetime.datetime.now().month
        context["activeYear"] = datetime.datetime.now().year
        context["activeDay"] = datetime.datetime.now().day
        return context

@method_decorator(login_required, name='dispatch')
class MonthView(DayFormView, ListView):
    model = Month
    template_name = "app/month.html"

    def get_queryset(self):
        year = datetime.datetime.now().year
        if "year" in self.kwargs:
            year = self.kwargs['year']

        list = Month.objects.filter(year__year=year)
        return list

    def get_context_data(self,*,object_list=None,  **kwargs):
        if not hasattr(self, "object_list"):
            self.object_list = self.model.objects.filter(year__year=self.kwargs['year'])

        context = super().get_context_data(object_list=self.object_list,**kwargs)
        context["activeMonth"] = datetime.datetime.now().month
        context["activeYear"] = datetime.datetime.now().year
        context["activeDay"] = datetime.datetime.now().day
        if "month" in self.kwargs:
            context["activeMonth"] = self.kwargs["month"]
        if "year" in self.kwargs:
            context["activeYear"] = self.kwargs['year']
        #context['form'] = DayForm()
        return context




