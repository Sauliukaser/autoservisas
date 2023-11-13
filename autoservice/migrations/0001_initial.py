# Generated by Django 4.2.7 on 2023-11-07 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutomobilioModelis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100, verbose_name='Marke')),
                ('modelis', models.CharField(max_length=100, verbose_name='Modelis')),
            ],
        ),
        migrations.CreateModel(
            name='Automobilis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_plate', models.CharField(max_length=10, verbose_name='Valstybinis Nr.')),
                ('vin_code', models.CharField(max_length=20, verbose_name='VIN kodas')),
                ('cliet', models.CharField(help_text='Vardas/Pavarde', max_length=100, verbose_name='Klientas')),
                ('car_model_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.automobiliomodelis')),
            ],
        ),
        migrations.CreateModel(
            name='Paslauga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Pavadinimas')),
                ('price', models.IntegerField(verbose_name='Kaina')),
            ],
        ),
        migrations.CreateModel(
            name='Uzsakymas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Data')),
                ('car_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.automobilis')),
            ],
        ),
        migrations.CreateModel(
            name='UzsakymoEilute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=5, verbose_name='Kiekis')),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.uzsakymas')),
                ('service_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservice.paslauga')),
            ],
        ),
    ]