# Generated by Django 5.0.4 on 2024-04-12 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='identifier',
            new_name='username',
        ),
    ]