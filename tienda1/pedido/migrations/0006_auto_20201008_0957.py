# Generated by Django 3.0.6 on 2020-10-08 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0005_auto_20201008_0942'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoria',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='articulos',
            old_name='categoria',
            new_name='category',
        ),
    ]
