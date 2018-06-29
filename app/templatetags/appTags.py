from django import template
from django.template.loader import get_template
import datetime, calendar
from app.models import Month


register = template.Library()


@register.inclusion_tag(get_template('app/daysInMonth.html'), takes_context=True)
def display_calendar(context, month:Month, year):
    #weekDisplayInMonth = calendar.monthcalendar(month=month.month, year=year)
    context["weekDisplayInMonth"] = month.day_set.all()
    #seg, ter, qua, qui, sex, sab, dom

    return context


@register.inclusion_tag(get_template('app/days.html'), takes_context=True)
def display_days(context, month:Month, year):

    weekDisplayInMonth = calendar.monthcalendar(month=month.month, year=year)
    days = month.day_set.all()
    lis = []
    for i,week in enumerate(weekDisplayInMonth):
        lis.append([])
        for d in week:
            if d != 0:
                d = days.get(day=d)
            lis[i].append(d)



    context["weeksOnMonth"] = lis
    context["weekSiglas"] = ["M", "T", "W", "T", "F", "S", "S"]

    #seg, ter, qua, qui, sex, sab, dom

    return context

