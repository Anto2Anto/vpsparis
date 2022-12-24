from .forms import ContactForm
from .models import *

menu = [
        {'title': "Page d'accueil", 'url_name': 'home'},
        # {'title': 'Services', 'url_name': 'service'},
        # {'title': 'Cle en main', 'url_name': 'cle_en_main'},
        # {'title': 'Contact', 'url_name': 'contact'},
]

personal_menu = [
        #{'title': 'Panier', 'url_name': 'cart'},
        {'title': 'Commandes en cours', 'url_name': 'current'},
        {'title': 'Historique de commandes', 'url_name': 'history'},
        {'title': 'Les favoris', 'url_name': 'favourite'},
        {'title': 'Parametres de profil', 'url_name': 'parametres'},
]


class DataMixin:
        def get_user_context(self, **kwargs):
                context = kwargs
                cats = Service_cat.objects.all()
                service = Service.objects.all()
                cem_cats = Cle_en_main_cat.objects.all()
                cem = Cle_en_main.objects.all()
                #contact_form = ContactForm()
                context['menu'] = menu
                context['cats'] = cats
                context['cem_cats'] = cem_cats
                context['service'] = service
                context['cem'] = cem
                context['personal_menu'] = personal_menu
                #context['contact_form'] = contact_form
                if 'cat_selected' not in context:
                        context['cat_selected'] = 0
                return context
