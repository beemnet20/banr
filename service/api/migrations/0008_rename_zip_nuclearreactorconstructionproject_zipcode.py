# Generated by Django 5.1 on 2024-08-11 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_expenditure_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nuclearreactorconstructionproject',
            old_name='zip',
            new_name='zipcode',
        ),
    ]
