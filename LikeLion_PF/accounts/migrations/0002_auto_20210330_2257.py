# Generated by Django 3.1.7 on 2021-03-30 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='userid',
            new_name='username',
        ),
    ]
