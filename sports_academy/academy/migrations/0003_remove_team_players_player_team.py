# Generated by Django 5.1.1 on 2024-09-28 17:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0002_remove_player_address_remove_player_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='players',
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='academy.team'),
        ),
    ]
