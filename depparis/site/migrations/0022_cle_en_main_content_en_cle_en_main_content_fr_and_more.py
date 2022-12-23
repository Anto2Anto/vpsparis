# Generated by Django 4.1.3 on 2022-12-10 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avangard', '0021_alter_personal_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='cle_en_main',
            name='content_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cle_en_main',
            name='content_fr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cle_en_main',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cle_en_main',
            name='title_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cle_en_main_cat',
            name='content_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cle_en_main_cat',
            name='content_fr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cle_en_main_cat',
            name='name_en',
            field=models.CharField(db_index=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cle_en_main_cat',
            name='name_fr',
            field=models.CharField(db_index=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='content_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='content_fr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='title_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='service_cat',
            name='content_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service_cat',
            name='content_fr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service_cat',
            name='name_en',
            field=models.CharField(db_index=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='service_cat',
            name='name_fr',
            field=models.CharField(db_index=True, max_length=255, null=True),
        ),
    ]