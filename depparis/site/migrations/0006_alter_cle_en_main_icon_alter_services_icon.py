# Generated by Django 4.1.3 on 2022-11-14 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avangard', '0005_service_cat_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cle_en_main',
            name='icon',
            field=models.ImageField(null=True, upload_to='icons/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='services',
            name='icon',
            field=models.ImageField(null=True, upload_to='icons/%Y/%m/%d'),
        ),
    ]