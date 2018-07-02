from django.urls import path, include
from .views import *


urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('validate/login/', LoginView.as_view(), name="validateLogin"),

    path('password_reset/', PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset/done/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),


]