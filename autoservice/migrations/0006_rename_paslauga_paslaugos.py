# Generated by Django 4.2.7 on 2023-11-07 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0005_rename_automobiliomodelis_automobiliumodeliai'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Paslauga',
            new_name='Paslaugos',
        ),
    ]