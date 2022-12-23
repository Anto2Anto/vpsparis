# Generated by Django 4.1.3 on 2022-11-27 08:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('avangard', '0010_alter_cle_en_main_cle_en_main_cat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cle_en_main',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cle_en_main_cat',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service_cat',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
            preserve_default=False,
        ),
    ]
