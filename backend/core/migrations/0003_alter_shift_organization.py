# Generated by Django 5.0.4 on 2024-08-11 21:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_orgs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.orgs'),
        ),
    ]
