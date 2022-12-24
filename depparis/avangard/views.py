from django.contrib.auth import logout, login
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import *
from .serializers import *
from .utils import *


# render is for templates
class RegisterUser(DataMixin, CreateView):
        form_class = RegisterUserForm
        template_name = 'avangard/register.html'
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
                return redirect('home')


class LoginUser(DataMixin, LoginView):
        form_class = LoginUserForm
        template_name = 'avangard/login.html'
        
        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                c_def = self.get_user_context(title = 'Autorisation')
                return dict(
                        list(context.items()) + list(c_def.items())
                )
        
        def get_success_url(self):
                return reverse_lazy('home')


def logout_user(request):
        logout(request)
        return redirect('home')


def about(request):
        return render(
                request,
                'avangard/about.html',
                context = {
                        'menu': menu,
                        'title': 'A propos'
                })


class PersonalViewSet(viewsets.ModelViewSet):
        queryset = Personal.objects.all()
        serializer_class = PersonalSerializer
        permission_classes = (AllowAny,)
        
        @action(methods = ['get'], detail = False)
        def current(self, request, *args, **kwargs):
                personal = Personal.objects.all()
                # return render(
                #         request,
                #         'avangard/personal_current.html',
                #         context = {
                #                 'menu': menu,
                #                 'personal_menu': personal_menu,
                #                 'title': 'Commandes en cours',
                #         }
                # )
                return Response(
                        {'personal': [p.current_orders for p in personal]}
                )
        
        @action(methods = ['get'], detail = False)
        def history(self, request, *args, **kwargs):
                personal = Personal.objects.all()
                # return render(
                #         request,
                #         'avangard/personal_history.html',
                #         context = {
                #                 'menu': menu,
                #                 'personal_menu': personal_menu,
                #                 'title': 'Historique des commandes',
                #         }
                # )
                return Response(
                        {'personal': [p.order_history for p in personal]}
                )
        
        @action(methods = ['get'], detail = False)
        def favourite(self, request, *args, **kwargs):
                personal = Personal.objects.all()
                # return render(
                #         request,
                #         'avangard/personal_favourite.html',
                #         context = {
                #                 'menu': menu,
                #                 'personal_menu': personal_menu,
                #                 'title': 'Mes favoris',
                #         }
                # )
                return Response(
                        {'personal': [p.favourite for p in personal]}
                )
        
        @action(methods = ['get'], detail = False)
        def parameters(self, request, *args, **kwargs):
                personal = Personal.objects.all()
                # return render(
                #        request,
                #        'avangard/personal_settings.html',
                #        context = {
                #                'menu': menu,
                #                'personal_menu': personal_menu,
                #                'title': 'Parametres du profil',
                #        }
                # )
                return Response(
                        {'personal': [p.settings for p in personal]}
                )

        # def get(self, request):
        #        return render(
        #                request,
        #                'avangard/personal.html',
        #                context = {
        #                        'menu': menu,
        #                        'personal_menu': personal_menu,
        #                        'title': 'Mon compte',
        #                }
        #        )


class RegisterViewSet(viewsets.ModelViewSet):
        serializer_class = RegisterSerializer
        permission_classes = (AllowAny,)
        queryset = Personal.objects.all()
        success_url = reverse_lazy('login')
        
        def get(self, request, *args, **kwargs):
                form = RegisterUserForm()
                return render(
                        request,
                        'avangard/register.html',
                        context = {
                                'form': form,
                                'menu': menu,
                                'title': 'Inscription',
                        }
                )
        
        def post(self, request, *args, **kwargs):
                form = RegisterUserForm(request.POST)
                serializer_class = RegisterSerializer(data = request.data)
                if serializer_class.is_valid():
                        data = serializer_class.validated_data
                        username = data.get('username')
                        phone = data.get('phone')
                        email = data.get('email')
                        password1 = data.get('password1')
                        password2 = data.get('password2')
                        return Response({"success": "sent"})
                return render(
                        request,
                        'avangard/register.html',
                        context = {
                                'form': form,
                                'menu': menu,
                                'title': 'Inscription',
                        })
        
        def form_valid(self, form):
                user = form.save()
                login(self.request, user)
                return redirect('home')


class FeedbackAPI(APIView):
        serializer_class = FeedbackSerializer
        permission_classes = (AllowAny,)
        cats = Service_cat.objects.all()
        cem_cats = Cle_en_main_cat.objects.all()
        service = Service.objects.all()
        cem = Cle_en_main.objects.all()
        
        def get(self, request, *args, **kwargs):
                form = ContactForm()
                return render(request, 'avangard/index.html', context = {
                        'form': form,
                        'title': 'Depannage',
                        'cats': FeedbackAPI.cats,
                        'cem_cats': FeedbackAPI.cem_cats,
                        'service': FeedbackAPI.service,
                        'cem': FeedbackAPI.cem,
                })
        
        def post(self, request, *args, **kwargs):
                form = ContactForm(request.POST)
                serializer_class = FeedbackSerializer(data = request.data)
                if serializer_class.is_valid():
                        data = serializer_class.validated_data
                        name = data.get('name')
                        phone = data.get('phone')
                        from_email = data.get('email')
                        subject = data.get('theme')
                        message = data.get('message')
                        send_mail(f'De {name} | {phone} | {subject}', message, from_email,
                                  ['Anton.Suleimanov@gmail.com'])
                        return Response({"success": "sent"})
                return render(request, 'avangard/index.html', context = {
                        'form': form,
                        'title': 'Depannage',
                        'cats': FeedbackAPI.cats,
                        'cem_cats': FeedbackAPI.cem_cats,
                        'service': FeedbackAPI.service,
                        'cem': FeedbackAPI.cem,
                })


def pageNotFound(request, exception):
        return HttpResponseNotFound('<h1>Page not found</h1>')


class PersonalAPI(APIView):
        serializer_class = PersonalSerializer
        permission_classes = (IsAuthenticated,)
        
        def get(self, request, *args, **kwargs):
                return render(request, 'avangard/personal.html', context = {
                        'title': 'Mon compte',
                        'menu': menu,
                        'personal_menu': personal_menu,
                })


class PersonalCurrentAPI(APIView):
        serializer_class = PersonalSerializer
        permission_classes = (IsAuthenticated,)
        
        def get(self, request, *args, **kwargs):
                return render(request, 'avangard/personal_current.html', context = {
                        'title': 'Mes commandes en cours',
                        'menu': menu,
                        'personal_menu': personal_menu,
                })


class PersonalHistoryAPI(APIView):
        serializer_class = PersonalSerializer
        permission_classes = (IsAuthenticated,)
        
        def get(self, request, *args, **kwargs):
                return render(request, 'avangard/personal_history.html', context = {
                        'title': 'Historique de mes commandes',
                        'menu': menu,
                        'personal_menu': personal_menu,
                })


class PersonalFavouriteAPI(APIView):
        serializer_class = PersonalSerializer
        permission_classes = (IsAuthenticated,)
        
        def get(self, request, *args, **kwargs):
                return render(request, 'avangard/personal_favourite.html', context = {
                        'title': 'Mes favoris',
                        'menu': menu,
                        'personal_menu': personal_menu,
                })


class PersonalParametresAPI(APIView):
        serializer_class = PersonalSerializer
        permission_classes = (IsAuthenticated,)
        
        def get(self, request, *args, **kwargs):
                return render(request, 'avangard/personal_settings.html', context = {
                        'title': 'Parametres du profil',
                        'menu': menu,
                        'personal_menu': personal_menu,
                })