# Generated by Django 4.1.3 on 2022-11-06 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formulator', '0012_remove_ingredient_formulation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulation',
            name='instruction_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='formulator.instruction'),
        ),
    ]
