from django.contrib.auth import logout, login
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView
from .forms import *
from .serializers import *
from .utils import *


class ContactFormView(DataMixin, FormView):
        form_class = ContactForm
        template_name = 'index.html'
        success_url = reverse_lazy('contact')  # home

        def get_context_data(self, *, object_list = None, **kwargs):
                context = super().get_context_data(**kwargs)
                c_def = self.get_user_context(title = 'Depannage')
                return dict(
                        list(context.items()) + list(c_def.items())
                )

        def form_valid(self, form):
                # print(form.cleaned_data)
                return redirect('contact')


# render is for templates
class RegisterUser(DataMixin, CreateView):
        form_class = RegisterUserForm
        template_name = 'register.html'
        success_url = reverse_lazy('login')
        
        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                c_def = self.get_user_context(title = 'Inscription')
                return dict(
                        list(context.items()) + list(c_def.items())
                )
        
        def form_valid(self, form):
                user = form.save()
                login(self.request, user)
                return redirect('contact')


class LoginUser(DataMixin, LoginView):
        form_class = LoginUserForm
        template_name = 'login.html'
        
        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                c_def = self.get_user_context(title = 'Autorisation')
                return dict(
                        list(context.items()) + list(c_def.items())
                )
        
        def get_success_url(self):
                return reverse_lazy('contact')


def logout_user(request):
        logout(request)
        return redirect('contact')


def about(request):
        return render(
                request,
                'about.html',
                context = {
                        'menu': menu,
                        'title': 'A propos'
                })


def pageNotFound(request, exception):
        return HttpResponseNotFound('<h1>Page not found</h1>')


