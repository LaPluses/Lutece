# Generated by Django 2.0.4 on 2018-05-10 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20180508_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='company',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='location',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='school',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]