# Generated by Django 2.0.5 on 2018-07-17 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedbapp', '0003_auto_20180717_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Released',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Year',
            field=models.TextField(blank=True),
        ),
    ]
