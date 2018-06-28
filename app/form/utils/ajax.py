from django.http import JsonResponse
from app.models import Day

class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class DayAjaxableResponseMixin:

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            data = {
                "errors": form.errors,
                "validate": False
            }
            return JsonResponse(data, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super().form_valid(form)

        if self.request.is_ajax():
            data = {
                "validate" : True
            }
            if int(form.data["spent"]) > 300:
                data["validate"] = False
            print(response)

            return JsonResponse(data=data)
        else:
            day = self.kwargs["day"]
            month = self.kwargs["month"]
            year = self.kwargs["year"]
            dayObject = Day.objects.get(day=day,month__month=month, month__year__year=year)
            dayObject.spent = form.data['spent']
            dayObject.save()
            return response