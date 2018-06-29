from django.views.generic import ListView
from .models import Day, Month, Year
from .form.forms import DayFormView, MonthFormView
import datetime, calendar
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect, JsonResponse

# Create your views here.

@method_decorator(login_required, name='dispatch')
class YearView(MonthFormView, ListView):
    model = Year
    template_name = "app/calendar.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["activeYear"] = datetime.datetime.now().year
        context["activeMonth"] = datetime.datetime.now().month

        context["currentMonth"] = datetime.datetime.now().month
        context["currentYear"] = datetime.datetime.now().year
        context["currentDay"] = datetime.datetime.now().day

        if "year" in self.kwargs:
            context["activeYear"] = self.kwargs['year']

        return context




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
        context["activeYear"] = datetime.datetime.now().year
        context["activeMonth"] = datetime.datetime.now().month

        context["currentMonth"] = datetime.datetime.now().month
        context["currentYear"] = datetime.datetime.now().year
        context["currentDay"] = datetime.datetime.now().day
        if "month" in self.kwargs:
            context["activeMonth"] = self.kwargs["month"]
        if "year" in self.kwargs:
            context["activeYear"] = self.kwargs['year']


        context["is_mobile"] = self.request.user_agent.is_mobile

        return context

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

        return response




