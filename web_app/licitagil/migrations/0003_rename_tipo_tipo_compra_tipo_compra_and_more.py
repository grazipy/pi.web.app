# Generated by Django 4.2 on 2023-05-28 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licitagil', '0002_tipo_compra_tipo_envio_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipo_compra',
            old_name='tipo',
            new_name='tipo_compra',
        ),
        migrations.RenameField(
            model_name='tipo_envio',
            old_name='tipo',
            new_name='tipo_envio',
        ),
    ]