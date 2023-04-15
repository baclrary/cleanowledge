from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views


urlpatterns = [
    path(
        "log-in/",
        LoginView.as_view(template_name="registration/log-in.html", redirect_authenticated_user=True),
        name="log-in",
    ),
    path("sign-up/", views.SignUpView.as_view(), name="sign-up"),
    path("log-out/", LogoutView.as_view(), name="log-out"),
]
