from django.contrib.auth import views as auth_views
from user.form.utils.ajax import UserAjaxableResponseMixin


# Create your views here.
class LoginView(UserAjaxableResponseMixin, auth_views.LoginView):
    template_name = 'user/login.html'

class LogoutView(auth_views.LogoutView):
    next_page = 'login'


class PasswordResetView(auth_views.PasswordResetView):
    email_template_name = 'user/password_reset_email.html'
    subject_template_name = 'user/password_reset_subject.txt'
    template_name = 'user/password_reset.html'

class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'user/password_reset_done.html'

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'user/password_reset_confirm.html'

class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'user/password_reset_complete.html'