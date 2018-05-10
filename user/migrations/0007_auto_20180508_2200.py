# Generated by Django 2.0.4 on 2018-05-08 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0002_remove_problem_sample_explanation'),
        ('user', '0006_auto_20180508_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usersolveinfo',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('ac', models.IntegerField(default=0, verbose_name='Accepted')),
                ('wa', models.IntegerField(default=0, verbose_name='Wrong Answer')),
                ('tle', models.IntegerField(default=0, verbose_name='Time Limit Exceeded')),
                ('mle', models.IntegerField(default=0, verbose_name='Memory Limit Exceeded')),
                ('ole', models.IntegerField(default=0, verbose_name='Output Limit Exceeded')),
                ('ce', models.IntegerField(default=0, verbose_name='Compile Error')),
                ('problem', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='problem.Problem')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='display_name',
            field=models.CharField(max_length=16),
        ),
    ]