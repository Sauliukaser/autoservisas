# Generated by Django 4.2.7 on 2023-11-11 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0013_alter_uzsakymas_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uzsakymoeilute',
            name='service_id',
        ),
        migrations.AddField(
            model_name='uzsakymoeilute',
            name='service_id',
            field=models.ManyToManyField(to='autoservice.paslaugos'),
        ),
    ]
