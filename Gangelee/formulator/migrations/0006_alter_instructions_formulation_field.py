# Generated by Django 4.1.3 on 2022-11-05 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formulator', '0005_remove_ingredients_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructions',
            name='formulation_field',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='formulator.formulation'),
        ),
    ]