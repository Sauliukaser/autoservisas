# Generated by Django 4.2.7 on 2023-11-15 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0017_uzsakymas_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='uzsakymas',
            name='due_back',
            field=models.DateField(blank=True, null=True, verbose_name='Grazinti iki'),
        ),
    ]
