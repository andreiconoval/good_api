# Generated by Django 2.2.5 on 2019-10-21 08:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='coord',
        ),
        migrations.AddField(
            model_name='coord',
            name='city',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to='cities.City'),
            preserve_default=False,
        ),
    ]
