# Generated by Django 4.1.3 on 2022-11-06 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formulator', '0015_product_formulation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingredient',
            new_name='Raw_Materials',
        ),
    ]
