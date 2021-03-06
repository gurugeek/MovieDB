# Generated by Django 2.0.5 on 2018-07-17 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedbapp', '0002_auto_20180713_1858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='title',
            new_name='Title',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='title',
        ),
        migrations.AddField(
            model_name='movie',
            name='Director',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='movie',
            name='Genre',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='movie',
            name='Plot',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='movie',
            name='Poster',
            field=models.URLField(default='http://google.com/'),
        ),
        migrations.AddField(
            model_name='movie',
            name='Released',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='movie',
            name='Title',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='movie',
            name='Year',
            field=models.IntegerField(default='0'),
        ),
    ]
