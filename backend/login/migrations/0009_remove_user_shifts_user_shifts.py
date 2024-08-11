# Generated by Django 5.0.4 on 2024-08-11 22:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_org_shifts'),
        ('login', '0008_user_shifts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='shifts',
        ),
        migrations.AddField(
            model_name='user',
            name='shifts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.shift'),
        ),
    ]