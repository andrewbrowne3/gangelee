# Generated by Django 4.1.3 on 2022-11-05 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formulator', '0004_alter_ingredients_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredients',
            name='Code',
        ),
    ]
