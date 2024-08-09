# Generated by Django 5.1 on 2024-08-08 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor',
            name='contact_person',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contractor',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contractor',
            name='phone_number',
            field=models.CharField(default='', max_length=12),
            preserve_default=False,
        ),
    ]
