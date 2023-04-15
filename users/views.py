from django.contrib.auth import get_user_model, login
from django.forms import ModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView

from . import forms


User = get_user_model()


class SignUpView(FormView):
    template_name = "registration/sign-up.html"
    form_class = forms.UserSignUpForm
    success_url = reverse_lazy("home")

    def form_valid(self, form: ModelForm) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
