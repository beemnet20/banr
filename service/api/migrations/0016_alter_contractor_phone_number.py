# Generated by Django 5.1 on 2024-08-12 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_expenditure_date_incurred'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
