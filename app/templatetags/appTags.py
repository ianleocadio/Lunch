from django import template
import datetime

register = template.Library()

@register.simple_tag(takes_context=True)
def current_time(month, year, context, format_string):

    return (month,year)