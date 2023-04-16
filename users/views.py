from typing import Any, Callable, Union

from django.contrib.auth import get_user_model, login
from django.forms import ModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView

from . import forms


User = get_user_model()


class SignUpView(FormView):
    template_name = "registration/sign-up.html"
    form_class = forms.UserSignUpForm
    success_url = reverse_lazy("home")
    redirect_authenticated_user = True

    def form_valid(self, form: ModelForm) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> Union[Callable, HttpResponse]:
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your `success_url` doesn't point to a signup page."
                )
            return HttpResponseRedirect(redirect_to)
        return super().dispatch(request, *args, **kwargs)


class ProfileView(DetailView):
    template_name = "profile.html"
    context_object_name = "profile"
    model = User
