# Generated by Django 5.0.4 on 2024-08-11 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_org_shifts'),
        ('login', '0009_remove_user_shifts_user_shifts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='shifts',
        ),
        migrations.AddField(
            model_name='user',
            name='shifts',
            field=models.ManyToManyField(blank=True, related_name='shifts_worked_by_user', to='core.shift'),
        ),
    ]
