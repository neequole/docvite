# Generated by Django 2.0 on 2017-12-07 08:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0004_invitation_is_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
