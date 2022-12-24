from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
        fields = ('title', 'content')
        

@register(Service_cat)
class Service_catTranslationOptions(TranslationOptions):
        fields = ('name', 'content')
        

@register(Cle_en_main)
class Cle_en_mainTranslationOptions(TranslationOptions):
        fields = ('title', 'content')


@register(Cle_en_main_cat)
class Cle_en_main_catTranslationOptions(TranslationOptions):
        fields = ('name', 'content')
        