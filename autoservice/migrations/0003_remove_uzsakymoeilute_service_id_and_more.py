# Generated by Django 4.2.7 on 2023-11-07 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0002_automobiliomodelis_variklis_automobiliomodelis_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uzsakymoeilute',
            name='service_id',
        ),
        migrations.AddField(
            model_name='uzsakymoeilute',
            name='service_id',
            field=models.ManyToManyField(to='autoservice.paslauga'),
        ),
    ]
