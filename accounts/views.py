from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignUpForm


class Login(auth_views.LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'sign_up.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        return render(self.request, 'sign_up.html', context={'success': True, 'form': self.form_class()})


class Logout(auth_views.LogoutView):
    next_page = reverse_lazy('login')
