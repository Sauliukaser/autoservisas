# Generated by Django 4.2.7 on 2023-11-09 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0009_alter_automobilis_vin_code_alter_uzsakymas_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='uzsakymas',
            name='status',
            field=models.CharField(blank=True, choices=[('d', 'Laukiama detaliu'), ('r', 'Remontuojama'), ('a', 'Atlikta'), ('p', 'Priimtas uzsakymas')], default='p', help_text='Uzsakymo statusas', max_length=1),
        ),
    ]
