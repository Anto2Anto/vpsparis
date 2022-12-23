# Generated by Django 4.1.3 on 2022-12-05 19:17

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avangard', '0020_alter_personal_options_personal_password1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='username',
            field=models.CharField(db_index=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=255, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='Nom'),
        ),
    ]
