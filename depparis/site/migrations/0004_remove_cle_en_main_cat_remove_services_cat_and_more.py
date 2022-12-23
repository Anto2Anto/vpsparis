# Generated by Django 4.1.3 on 2022-11-14 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avangard', '0003_cle_en_main_cat_rename_category_service_cat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cle_en_main',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='services',
            name='cat',
        ),
        migrations.AddField(
            model_name='cle_en_main',
            name='cle_en_main_cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='avangard.cle_en_main_cat'),
        ),
        migrations.AddField(
            model_name='services',
            name='service_cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='avangard.service_cat'),
        ),
    ]
