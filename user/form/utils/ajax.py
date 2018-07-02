from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class UserAjaxableResponseMixin:


    def form_invalid(self, form):
        response = super().form_invalid(form)
        data = {}
        if self.request.is_ajax():

            try:
                user = User.objects.get(username=form.data["user"])
                return JsonResponse(data)
            except ObjectDoesNotExist:
                data = {
                    "errors": ["User does not exist"]
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