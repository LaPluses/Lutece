# Generated by Django 2.0.4 on 2018-04-27 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='standard_input',
            field=models.CharField(blank=True, max_length=1024),
        ),
        migrations.AddField(
            model_name='problem',
            name='standard_output',
            field=models.CharField(blank=True, max_length=1024),
        ),
    ]