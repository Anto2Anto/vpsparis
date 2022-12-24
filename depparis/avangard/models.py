from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.urls import reverse


class Service_cat(models.Model):  # list of services
        name = models.CharField(max_length = 255, db_index = True)
        slug = models.SlugField(max_length = 255, unique = True, db_index = True)
        content = models.TextField(blank = True)
        is_published = models.BooleanField(default = True)
        user = models.ForeignKey(User, verbose_name = 'User', on_delete = models.CASCADE)
        
        def __str__(self):
                return self.name
        
        def get_absolute_url(self):
                return reverse('Service_cat', kwargs = {'service_cat_slug': self.slug})
        
        class Meta:
                verbose_name = 'Categorie des services'
                verbose_name_plural = 'Categories des services'
                ordering = ['id']


class Service(models.Model):  # services themselves listed on the main page
        title = models.CharField(max_length = 255)
        slug = models.SlugField(max_length = 255, unique = True, db_index = True, null = True)
        icon = models.ImageField(upload_to = 'icons/%Y/%m/%d', null = True,
                                 blank = True)  # icon - leads to the specific page of the service
        content = models.TextField(blank = True)
        time_create = models.DateTimeField(auto_now_add = True)
        time_update = models.DateTimeField(auto_now = True)
        is_published = models.BooleanField(default = True)
        service_cat = models.ForeignKey('Service_cat', on_delete = models.CASCADE, null = True)
        user = models.ForeignKey(User, verbose_name = 'User', on_delete = models.CASCADE)
        
        def __str__(self):
                return self.title
        
        def get_absolute_url(self):
                return reverse('service', kwargs = {'service_slug': self.slug})
        
        class Meta:
                verbose_name = 'Service'
                verbose_name_plural = 'Services'
                ordering = ['title']


class Cle_en_main(models.Model):  # cles_en_main themselves listed on the main page
        title = models.CharField(max_length = 255)
        slug = models.SlugField(max_length = 255, unique = True, db_index = True, null = True)
        icon = models.ImageField(upload_to = 'icons/%Y/%m/%d', null = True,
                                 blank = True)  # icon - leads to the specific page of the service
        content = models.TextField(blank = True)
        time_create = models.DateTimeField(auto_now_add = True)
        time_update = models.DateTimeField(auto_now = True)
        is_published = models.BooleanField(default = True)
        cle_en_main_cat = models.ForeignKey('Cle_en_main_cat', on_delete = models.CASCADE, null = True)
        user = models.ForeignKey(User, verbose_name = 'User', on_delete = models.CASCADE)
        
        def __str__(self):
                return self.title
        
        def get_absolute_url(self):
                return reverse('Cle_en_main', kwargs = {'cle_en_main_slug': self.slug})
        
        class Meta:
                verbose_name = 'Cle en main'
                verbose_name_plural = 'Cle en main'
                ordering = ['title']


class Cle_en_main_cat(models.Model):  # list of services
        name = models.CharField(max_length = 255, db_index = True)
        slug = models.SlugField(max_length = 255, unique = True, db_index = True)
        content = models.TextField(blank = True)
        is_published = models.BooleanField(default = True)
        user = models.ForeignKey(User, verbose_name = 'User', on_delete = models.CASCADE)
        
        def __str__(self):
                return self.name
        
        def get_absolute_url(self):
                return reverse('Cle_en_main_cat', kwargs = {'cle_en_main_cat_slug': self.slug})
        
        class Meta:
                verbose_name = 'Categorie des cle en main'
                verbose_name_plural = 'Categories des cle en main'
                ordering = ['id']


class Personal(models.Model):
        username_validator = UnicodeUsernameValidator()
        username = models.CharField(
                max_length = 255,
                verbose_name = 'Nom',
                db_index = True,
                unique = True,
                help_text = (
                        "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
                ),
                validators = [username_validator],
                error_messages = {
                        "unique": "A user with that username already exists.",
                },
        )
        email = models.EmailField(
                max_length = 255,
                db_index = False,
                verbose_name = 'E-mail'
        )
        phone = models.CharField(
                max_length = 255,
                db_index = True,
                verbose_name = 'Numero de telephone'
        )
        password1= models.CharField(
                max_length = 255,
                verbose_name = 'Mot de passe'
        )
        password2 = models.CharField(
                max_length = 255,
                verbose_name = 'Mot de passe confirmer'
        )
        current_orders = models.CharField(
                max_length = 255,
                blank = True,
                db_index = True,
                verbose_name = 'Commandes en cours'
        )
        order_history = models.CharField(
                max_length = 255,
                blank = True,
                db_index = True,
                verbose_name = 'Historique de commandes'
        )
        favourite = models.CharField(
                max_length = 255,
                blank = True,
                db_index = True,
                verbose_name = 'Les favoris'
        )
        settings = models.CharField(
                max_length = 255,
                blank = True,
                verbose_name = 'Parametres de profil'
        )
        
        def __str__(self):
                return self.username
        
        def get_absolute_url(self):
                return reverse('personal')

        EMAIL_FIELD = "email"
        USERNAME_FIELD = "username"
        
        class Meta:
                verbose_name = 'Personal'
                verbose_name_plural = 'Personal'
                ordering = ['id']
