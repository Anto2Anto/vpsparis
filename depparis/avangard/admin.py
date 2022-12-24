from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

from .models import *


class PersonalAdmin(admin.ModelAdmin):
        list_display = ('id', 'username', 'email', 'phone', 'current_orders',
                        'order_history', 'favourite', 'settings')
        list_display_links = ('id', 'username')
        search_fields = ('username', 'email', 'phone', 'current_orders',
                         'order_history')
        list_editable = ('phone',)
        list_filter = ('username', 'phone', 'current_orders', 'order_history')
        fields = ('username', 'email', 'phone', 'current_orders',
                  'order_history', 'favourite', 'settings')
        readonly_fields = ('order_history', 'favourite')


class ServicesAdmin(TranslationAdmin):  # admin.ModelAdmin
        list_display = ('id', 'title', 'slug', 'content', 'time_create', 'time_update', 'is_published', 'service_cat')
        list_display_links = ('id', 'title')
        search_fields = ('title', 'content')
        list_editable = ('content', 'is_published')
        list_filter = ('service_cat', 'is_published', 'time_create', 'time_update')
        prepopulated_fields = {'slug': ('title',)}
        fields = ('title', 'slug', 'content', 'service_cat', 'icon', 'get_html_icon',
                  'is_published', 'time_create', 'time_update')
        readonly_fields = ('time_create', 'time_update', 'get_html_icon')
        save_on_top = False
        
        def get_html_icon(self, object):
                if object.icon:
                        return mark_safe(f'<img src="{object.icon.url}" width=20>')
        
        get_html_icon.short_description = 'Icon'


class CleEnMainAdmin(TranslationAdmin):  # admin.ModelAdmin
        list_display = ('id', 'title', 'slug', 'content', 'time_create',
                        'time_update', 'is_published', 'cle_en_main_cat')
        list_display_links = ('id', 'title')
        search_fields = ('title', 'content')
        list_editable = ('content', 'is_published')
        list_filter = ('cle_en_main_cat', 'is_published', 'time_create', 'time_update')
        prepopulated_fields = {'slug': ('title',)}
        fields = ('title', 'slug', 'content', 'cle_en_main_cat', 'icon', 'get_html_icon',
                  'is_published', 'time_create', 'time_update')
        readonly_fields = ('time_create', 'time_update', 'get_html_icon')
        save_on_top = False
        
        def get_html_icon(self, object):
                if object.icon:
                        return mark_safe(f'<img src="{object.icon.url}" width=20>')
        
        get_html_icon.short_description = 'Icon'


class ServiceCatAdmin(TranslationAdmin):  # admin.ModelAdmin
        list_display = ('id', 'name', 'content', 'is_published')
        list_display_links = ('id', 'name')
        search_fields = ('name',)
        # list_filter = ('id', 'name')
        prepopulated_fields = {'slug': ('name',)}
        save_on_top = False


class CleEnMainCatAdmin(TranslationAdmin):  # admin.ModelAdmin
        list_display = ('id', 'name', 'content', 'is_published')
        list_display_links = ('id', 'name')
        search_fields = ('name',)
        # list_filter = ('id', 'name')
        prepopulated_fields = {'slug': ('name',)}
        save_on_top = False


admin.site.register(Service, ServicesAdmin)
admin.site.register(Cle_en_main, CleEnMainAdmin)
admin.site.register(Service_cat, ServiceCatAdmin)
admin.site.register(Cle_en_main_cat, CleEnMainCatAdmin)
admin.site.register(Personal, PersonalAdmin)

admin.site.site_header = 'Depannage administration'
admin.site.site_title = 'Depannage administration'
