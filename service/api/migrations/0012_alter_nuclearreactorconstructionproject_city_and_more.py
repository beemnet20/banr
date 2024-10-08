# Generated by Django 5.1 on 2024-08-12 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_nuclearreactorconstructionproject_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nuclearreactorconstructionproject',
            name='city',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='nuclearreactorconstructionproject',
            name='contractors',
            field=models.ManyToManyField(blank=True, null=True, related_name='projects', to='api.contractor'),
        ),
        migrations.AlterField(
            model_name='nuclearreactorconstructionproject',
            name='state',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='nuclearreactorconstructionproject',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
