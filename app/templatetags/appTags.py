from django import template
from django.template.loader import get_template
import datetime, calendar
from app.models import Month

register = template.Library()

@register.inclusion_tag(filename=get_template('daysInMonth.html'), takes_context=True, name="calendar")
def display_calendar(context, month:Month, year):
    #month = context[""]
    #weekDisplayInMonth = calendar.monthcalendar(month=month.month, year=year)
    #print(weekDisplayInMonth)

    return context

