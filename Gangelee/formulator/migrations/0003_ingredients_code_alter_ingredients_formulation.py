# Generated by Django 4.1.3 on 2022-11-05 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formulator', '0002_formulation_ingredients_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredients',
            name='Code',
            field=models.IntegerField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='Formulation',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='formulator.formulation'),
        ),
    ]
