# Generated by Django 4.2.7 on 2023-11-09 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0011_alter_uzsakymas_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automobilis',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='uzsakymoeilute',
            name='amount',
            field=models.CharField(blank=True, max_length=5, verbose_name='Kiekis'),
        ),
    ]
