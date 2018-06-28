from cgitb import reset

from django.http import JsonResponse
from app.models import Day

class DayAjaxableResponseMixin:


    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            data = {
                "errors": form.errors,
                "validate": False
            }
            return JsonResponse(data, status=400)

        return response

    def form_valid(self, form):
        response = super().form_valid(form)

        if self.request.is_ajax():
            data = {
                "validate" : True
            }
            return JsonResponse(data=data)

        return response


class MonthAjaxableResponseMixin:

    def form_invalid(self, form):
        response = super().form_valid(form)

        if self.request.is_ajax():
            return response
        else:
            return None

    def form_valid(self, form):
        response = super().form_valid(form)

        if self.request.is_ajax():
            return JsonResponse(data={})
        else:
            return response