# Generated by Django 2.2.5 on 2019-10-21 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_auto_20191021_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='ow_id',
            field=models.IntegerField(default=0),
        ),
    ]