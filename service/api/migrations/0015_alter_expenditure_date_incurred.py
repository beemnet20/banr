# Generated by Django 5.1 on 2024-08-12 19:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_expenditure_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenditure',
            name='date_incurred',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
