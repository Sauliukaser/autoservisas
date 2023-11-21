# Generated by Django 4.2.7 on 2023-11-21 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0022_profilis'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profilis',
            options={'verbose_name': 'Profilis', 'verbose_name_plural': 'Profiliai'},
        ),
        migrations.AlterField(
            model_name='automobilis',
            name='cliet',
            field=models.CharField(help_text='First name/Last name', max_length=30, verbose_name='Customer'),
        ),
        migrations.AlterField(
            model_name='automobilis',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='covers', verbose_name='Cover'),
        ),
        migrations.AlterField(
            model_name='automobilis',
            name='number_plate',
            field=models.CharField(max_length=10, verbose_name='Number plate'),
        ),
        migrations.AlterField(
            model_name='automobilis',
            name='vin_code',
            field=models.CharField(blank=True, max_length=20, verbose_name='VIN code'),
        ),
    ]
